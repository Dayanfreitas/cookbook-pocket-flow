from pocketflow import Flow, BatchFlow, Node

def call_llm(prompt):
    return f"This is the summary of the file: {prompt}"

class SummarizeAllFiles(BatchFlow):
    # IMPORTANTE: Retornar uma lista de dicionários de parâmetros (não dados para processamento)

    def prep(self, shared):
        filenames = list(shared['data'].keys())
        
        return [{'filename': filename} for filename in filenames]


class LoadFile(Node):
    def prep(self, shared):
        print(self.params)

        filename = self.params['filename']
        return filename

    def exec(self, filename):
        with open(f"data/{filename}", 'r') as file:
            return file.read()

    def post(self, shared, prep_res, prep_result):
        shared['current_file_content'] = prep_result
        return 'default'

# Summarize node that works on the currently loaded file
class Summarize(Node):
    def prep(self, shared):
        return shared["current_file_content"]
        
    def exec(self, content):
        prompt = f"Summarize this file in 50 words: {content}"
        return call_llm(prompt)
        
    def post(self, shared, prep_res, exec_res):
        # Store summary in shared, indexed by current filename
        filename = self.params["filename"]  # Again, using params
        if "summaries" not in shared:
            shared["summaries"] = {}
        shared["summaries"][filename] = exec_res
        return "default"

shared = {
    'data': {
        'file1.txt': 'This is the first file',
        'file2.txt': 'This is the second file',
        'file3.txt': 'This is the third file',
    }
}

load_file = LoadFile()
summarize = Summarize()
load_file >> summarize

summarize_file = Flow(start=load_file)

# Wrap in a BatchFlow to process all files
summarize_all_files = SummarizeAllFiles(start=summarize_file)
summarize_all_files.run(shared)

print(shared['summaries'])

from pocketflow import Flow, BatchNode

# Aqui seria a tool que chama a LLM
def call_llm(prompt):
    return prompt

class MapSumarizer(BatchNode):
    def prep(self, shared):
        content = shared["data"]
        chunk_size = 10
        chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]
        return chunks

    def exec(self, prep_result):
        print(prep_result)
        prompt = f"Summarize this chunk in 10 words: {prep_result}"

        return call_llm(prompt)

    def post(self, shared, prep_result, exec_result_list):
        print(exec_result_list)
        combined = '\n'.join(exec_result_list)
        
        shared['summary'] = combined

        return 'default'

shared={
    "data": "SUPONHA QUE AQUI TENHA UM TEXTO MUITO GRANDE .... QUE VAI SER DIVIDIDO EM CHUNKS"}

map_sumarizer = MapSumarizer()
flow = Flow(start=map_sumarizer)
flow.run(shared)

print( shared['summary'])

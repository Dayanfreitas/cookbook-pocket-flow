#!/bin/bash

name_project=$1
echo "NAME PROJECT: $name_project"

mkdir -p $name_project
touch $name_project/.env

echo ".env" > $name_project/.gitignore

cd $name_project

cat <<EOF > Pipfile
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
python-dotenv = ">=0.19.0"
pocketflow = ">=0.0.2"

[dev-packages]

[requires]
python_version = "3.13"
EOF



echo """
print(\"Hello World\")
""" >> main.py

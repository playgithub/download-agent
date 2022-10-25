import string
import yaml

path = 'input.yml'

with open(path, 'r', encoding = 'utf-8') as f:
    file_content = f.read()

tempalte_file_content = string.Template(file_content)

yaml_input = yaml.safe_load(file_content)
versions = yaml_input['versions']

file_content = tempalte_file_content.safe_substitute(versions)

yaml_input = yaml.safe_load(file_content)

items = yaml_input['items']

with open('tmp/aria2c_input.txt', 'w', encoding = 'utf-8') as f:
    for item in items:
        url_with_newline = item['url'] + '\n'
        f.write(url_with_newline)

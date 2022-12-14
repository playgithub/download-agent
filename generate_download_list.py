import string
import yaml

with open('input.yml', 'r', encoding = 'utf-8') as f:
    file_content = f.read()

items = yaml.safe_load(file_content)

with open('./aria2c_input.txt', 'w', encoding = 'utf-8') as f:
    for item in items:
        string_tempalte_url = string.Template(item['url'])
        url_with_newline = string_tempalte_url.safe_substitute(item) + '\n'
        f.write(url_with_newline)
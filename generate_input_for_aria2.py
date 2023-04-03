import string
import yaml

def download(items):
    with open('./aria2c_input.txt', 'w', encoding = 'utf-8') as f:
        for item in items:
            if item['download']:
                string_tempalte_url = string.Template(item['url'])
                url = string_tempalte_url.safe_substitute(item)
                url_with_newline = url + '\n'
                f.write(url_with_newline)

with open('input.yml', 'r', encoding = 'utf-8') as f:
    file_content = f.read()

items = yaml.safe_load(file_content)

download(items)

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

def get_release_url_for_chromium(version):
    return 'https://github.com/playgithub/download-agent/releases/download/Downloads/chromium-' + version + '.tar.xz'

def get_release_url_for_vscodium(version):
    return 'https://github.com/VSCodium/vscodium/releases/download/' + version + '/VSCodium-linux-x64-' + version + '.tar.gz'

def show_url_on_github(items):
    for item in items:
        if item['show_url']:
            if item['name'] == 'chromium':
                print(get_release_url_for_chromium(item['version']))
            elif item['name'] == 'vscodium':
                print(get_release_url_for_vscodium(item['version']))

with open('input.yml', 'r', encoding = 'utf-8') as f:
    file_content = f.read()

items = yaml.safe_load(file_content)
download(items)
show_url_on_github(items)

    

import string
import yaml

def get_release_url(version):
    return 'https://github.com/playgithub/download-agent/releases/download/Downloads/chromium-' + version + '.tar.xz'

with open('input.yml', 'r', encoding = 'utf-8') as f:
    file_content = f.read()

items = yaml.safe_load(file_content)

for item in items:
    chromium_version = item['version']
    print(get_release_url(chromium_version))

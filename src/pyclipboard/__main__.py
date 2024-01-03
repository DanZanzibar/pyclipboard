import readline
import re
import os.path
import pyperclip
from pyclipboard.pyclipboard import complete, SNIPPET_DIR


readline.parse_and_bind('tab: complete')
readline.set_completer(complete)

snippet_name = input('Which snippet?\n> ')
snippet_path = os.path.join(SNIPPET_DIR, (snippet_name + '.txt'))

with open(snippet_path, 'r') as f:
    snippet = f.read()

readline.set_completer()

placeholders = re.findall(r'~!~[^(~!~)]*~!~', snippet)
finished_placeholders = []

for placeholder in placeholders:
    if placeholder not in finished_placeholders:
        new_text = input(placeholder[3: -3] + ': ')
        snippet = snippet.replace(placeholder, new_text)
        finished_placeholders.append(placeholder)

pyperclip.copy(snippet)

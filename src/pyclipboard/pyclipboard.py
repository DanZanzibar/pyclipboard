import os
import re
from subprocess import run, PIPE, DEVNULL


SNIPPET_DIR = "/home/zan/sync/dat/snippets/"

def dmenu_input(prompt: str) -> str:
    process = run(
        ['dmenu', '-p', prompt],
        stdin=DEVNULL,
        stdout=PIPE,
        text=True)

    return process.stdout.strip()

def snippet_names(snippet_dir: str) -> list[str]:
    return [file_name.split('.')[0]
            for file_name in os.listdir(snippet_dir)]
    
def choose_snippet(snippet_dir: str) -> str:
    snippets = snippet_names(snippet_dir)
    snippets = '\n'.join(snippets)
    process = run(
        ['dmenu', '-p', 'Which snippet?'],
        input=snippets,
        stdout=PIPE,
        text=True
    )

    snippet_name = process.stdout.strip()
    snippet_path = os.path.join(SNIPPET_DIR, (snippet_name + '.txt'))

    with open(snippet_path, 'r') as f:
        snippet = f.read()

    return snippet

def replace_placeholders(snippet: str) -> str:
    placeholders = re.findall(r'~!~[^(~!~)]*~!~', snippet)
    finished_placeholders = []

    for placeholder in placeholders:
        if placeholder not in finished_placeholders:
            new_text = dmenu_input(placeholder[3: -3] + ': ')
            snippet = snippet.replace(placeholder, new_text)
            finished_placeholders.append(placeholder)

    return snippet


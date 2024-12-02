import re
import pyperclip
from pyclipboard.dmenu import select_file_or_dir, dmenu_input


SNIPPET_PROMPT = 'Which snippet:'
SNIPPET_DIR = "/home/zan/sync/dat/snippets/"
PH_DELIM = '~!~'

def choose_snippet(snippet_dir: str) -> str:
    snippet_path = select_file_or_dir(SNIPPET_PROMPT, snippet_dir, recurse=True)
    with open(snippet_path, 'r') as f:
        snippet = f.read()

    return snippet

def replace_placeholders(snippet: str, ph_delim: str) -> str:
    ph_length = len(ph_delim)
    placeholders = re.findall(f'{ph_delim}[^({ph_delim})]*{ph_delim}', snippet)
    finished_placeholders = []
    
    for placeholder in placeholders:
        if placeholder not in finished_placeholders:
            new_text = dmenu_input(placeholder[ph_length: -ph_length] + ':')
            snippet = snippet.replace(placeholder, new_text)
            finished_placeholders.append(placeholder)

    return snippet

def copy_snippet(snippet_dir: str, ph_delim: str = PH_DELIM) -> None:
    snippet = choose_snippet(snippet_dir)
    snippet = replace_placeholders(snippet, ph_delim)
    pyperclip.copy(snippet)

def pyclipboard() -> None:
    copy_snippet(SNIPPET_DIR)

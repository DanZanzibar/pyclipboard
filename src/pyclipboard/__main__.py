import pyperclip
from pyclipboard.pyclipboard import SNIPPET_DIR, choose_snippet, replace_placeholders


snippet = choose_snippet(SNIPPET_DIR)
snippet = replace_placeholders(snippet)

pyperclip.copy(snippet)

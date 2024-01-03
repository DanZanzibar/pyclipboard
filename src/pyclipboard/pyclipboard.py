import os


SNIPPET_DIR = "/home/zan/sync-general/bin/snippets/"


snippets = [file_name.split('.')[0]
            for file_name in os.listdir(SNIPPET_DIR)]


def complete(text, state):
    if text == '':
        matches = snippets
    else:
        matches = [snip for snip in snippets if snip.startswith(text)]

    if state > len(matches):
        single_match = None
    else:
        single_match = matches[state]

    return single_match

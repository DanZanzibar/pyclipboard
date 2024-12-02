from subprocess import run, PIPE, DEVNULL
from os import listdir
from os.path import expanduser, isfile, isdir, join


FILE_DIR_PROMPT = 'Which file/directory:'
FILE_PROMPT = 'Which file:'
DIR_PROMPT = 'Which directory:'

def run_dmenu(prompt: str, options: list[str]) -> str:
    if options:
        standard_in = None
        text_input = '\n'.join(options)
    else:
        standard_in = DEVNULL
        text_input = None
        
    process = run(
        ['dmenu', '-p', prompt],
        input=text_input,
        stdin=standard_in,
        stdout=PIPE,
        text=True)

    return process.stdout.strip()

def dmenu_input(prompt: str) -> str:
    return run_dmenu(prompt, [])

def select_file(prompt: str = FILE_PROMPT, path: str = '.') -> str:
    files = [x for x in listdir(path) if isfile(x)]
    return run_dmenu(prompt, files)

def select_dir(prompt: str = DIR_PROMPT, path: str = '.') -> str:
    dirs = [x for x in listdir(path) if isdir(x)]
    return run_dmenu(prompt, dirs)

def select_file_or_dir(prompt: str = FILE_DIR_PROMPT, path: str = '.',
                       recurse: bool = False) -> str:
    path = expanduser(path)
    files_and_dirs = listdir(path)
    dirs = [x + '/' for x in files_and_dirs if isdir(join(path, x))]
    files = [x for x in files_and_dirs if isfile(join(path, x))]
    files_and_dirs = dirs + files

    selection = run_dmenu(prompt, files_and_dirs)
    if selection == '':
        return selection
    
    selection_path = join(path, selection)
    
    if (recurse and isdir(selection_path)):
        return select_file_or_dir(prompt, selection_path, recurse)
    else:
        return selection_path

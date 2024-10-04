import re
from pathlib import Path
from colorama import Fore


def parse_directory(pathname: str, recursive: bool = False, level: int = 0):
    '''Creates directory view for command line interface\n
    ARGS:
        pathname: str - path to the directory
        recursive: bool - true if there is requirement to enter inside direcories and check there
        level: int - nested level. always 0 when calling a function, changes within the function
    RETURNS:
        nothing. Simply it output names of dirs and files with differenet colors     
    '''
    if not level:
        print(Fore.GREEN + pathname + "/")
    
    for path in Path(pathname).iterdir():
        prefix = "  "
        name = path.as_posix().split("/")[-1]
    
        if path.is_dir():
            pattern = re.compile(r"__\w+__")
            if re.search(pattern, path.as_posix()):
                continue

            level += 1
            print(Fore.GREEN + prefix * level + name + Fore.RESET)
            
            if recursive:
                parse_directory(path.as_posix(), True, level)
                level -= 1
        else:
            level += 1
            print(Fore.CYAN + prefix * level + name + Fore.RESET)
            level -= 1

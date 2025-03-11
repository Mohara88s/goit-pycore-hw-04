import sys
from pathlib import Path
from colorama import Fore

def main():
    if len(sys.argv) > 1:
        print(sys.argv)
        directory = Path(sys.argv[1])
    else:
        print('No path in the request!')
        return
    
    if not directory.exists():
        print(f'The path {directory} does not exist!')
    elif directory.suffix:
        print(f'The path {directory} leads to a file!')
    else:
        print_directory(directory)

# Recursion function with colored print
def print_directory(direct, deep=0):
    print(f"{" "*4*deep}{Fore.BLUE}{direct.name}/{Fore.RESET}")
    for path in direct.iterdir():
        if path.is_dir():
            print_directory(path, deep+1)
        else:
            print(f"{" "*4*(deep+1)}{Fore.GREEN}{path.name}{Fore.RESET}")
    

if __name__ == "__main__":
    main()

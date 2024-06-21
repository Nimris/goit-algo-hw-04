import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def directory_content(path: Path) -> str:
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{Fore.RED} [FOLDER] {item.name} {Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN} [FILE] {item.name} {Style.RESET_ALL}")
    except:
        print("Smth went wrong")            

def main():
    if len(sys.argv) > 1:
        directory_path = Path(sys.argv[1])
    else:
        print("Enter the path: python main.py <path_to_directory>")
        
    if not directory_path.exists():
        print(f"Error: The path '{directory_path}' does not exist.")
        sys.exit(1)
        
    if not directory_path.is_dir():
        print(f"Error: The path '{directory_path}' is not a directory.")
        sys.exit(1)
        
    directory_content(directory_path)
    
if __name__ == "__main__":
    main()
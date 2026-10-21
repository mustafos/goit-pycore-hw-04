
import sys
from pathlib import Path

from colorama import Fore, Style, init


def print_directory_tree(path: Path, prefix: str = "") -> None:
    """Print directory contents as a colored tree."""
    try:
        entries = sorted(
            path.iterdir(),
            key=lambda entry: (entry.is_file(), entry.name.lower()),
        )
    except OSError as error:
        print(f"{Fore.RED}Cannot access {path}: {error}{Style.RESET_ALL}")
        return

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "
        next_prefix = prefix + ("    " if is_last else "│   ")

        if entry.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}{entry.name}/{Style.RESET_ALL}")
            print_directory_tree(entry, next_prefix)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")


def main():
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Usage: python hw03.py <directory_path>")
        return

    directory = Path(sys.argv[1]).expanduser()

    if not directory.exists():
        print(f"{Fore.RED}Error: path does not exist: {directory}")
        return

    if not directory.is_dir():
        print(f"{Fore.RED}Error: path is not a directory: {directory}")
        return

    print(f"{Fore.BLUE}{directory.name}/")
    print_directory_tree(directory)


if __name__ == "__main__":
    main()

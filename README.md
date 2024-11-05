# File Manager

## Description

This project is a file management script in Python. It allows you to create, delete, move, copy, rename, list, search, and display the content of files. It can also rename multiple files and folders in a directory.

## Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) for Python environment management

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/RitterAntoine/File_Manager
    cd File_Manager
    ```

2. Create and activate the virtual environment with `uv`:
    ```sh
    uv venv
    uv sync
    source .venv/bin/activate
    ```

## Usage

The `main.py` script accepts several actions via command line arguments. Here are the available actions:

- `create`: Create a new file
- `delete`: Delete a file
- `move`: Move a file
- `copy`: Copy a file
- `rename`: Rename a file
- `list`: List files in a directory
- `search`: Search for a file in a directory
- `show`: Display the content of a file
- `rename_multiple`: Rename multiple files and folders in a directory

### Examples

1. Create a file:
    ```sh
    uv run main.py create --src <file_path>
    ```

2. Delete a file:
    ```sh
    uv run main.py delete --src <file_path>
    ```

3. Move a file:
    ```sh
    uv run main.py move --src <source_path> --dst <destination_path>
    ```

4. Copy a file:
    ```sh
    uv run main.py copy --src <source_path> --dst <destination_path>
    ```

5. Rename a file:
    ```sh
    uv run main.py rename --src <old_name> --dst <new_name>
    ```

6. List files in a directory:
    ```sh
    uv run main.py list --directory <directory_path>
    ```

7. Search for a file in a directory:
    ```sh
    uv run main.py search --directory <directory_path> --filename <file_name>
    ```

8. Display the content of a file:
    ```sh
    uv run main.py show --src <file_path>
    ```

9. Rename multiple files and folders in a directory:
    ```sh
    uv run main.py rename_multiple --directory <directory_path> --old_char <old_character> --new_char <new_character> [--recursive]
    ```

## License

This project is open source. You are free to use, modify, and distribute it.
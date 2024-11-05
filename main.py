import os
import shutil
import sys
import argparse

def create_file(file_path):
    """Create a new file."""
    try:
        with open(file_path, 'w') as f:
            pass
        print(f"File '{file_path}' created successfully.")
    except Exception as e:
        print(f"Error creating file '{file_path}': {e}")

def delete_file(file_path):
    """Delete a file."""
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting file '{file_path}': {e}")

def move_file(src, dst):
    """Move a file."""
    try:
        shutil.move(src, dst)
        print(f"File moved from '{src}' to '{dst}' successfully.")
    except Exception as e:
        print(f"Error moving file from '{src}' to '{dst}': {e}")

def copy_file(src, dst):
    """Copy a file."""
    try:
        shutil.copy(src, dst)
        print(f"File copied from '{src}' to '{dst}' successfully.")
    except Exception as e:
        print(f"Error copying file from '{src}' to '{dst}': {e}")

def rename_file(src, dst):
    """Rename a file."""
    try:
        os.rename(src, dst)
        print(f"File renamed from '{src}' to '{dst}' successfully.")
    except Exception as e:
        print(f"Error renaming file from '{src}' to '{dst}': {e}")

def list_files(directory):
    """List files in a directory."""
    try:
        files = os.listdir(directory)
        print("Files in directory:", files)
    except Exception as e:
        print(f"Error listing files in directory '{directory}': {e}")

def search_files(directory, filename):
    """Search for a file in a directory."""
    try:
        for root, dirs, files in os.walk(directory):
            if filename in files:
                print("File found at:", os.path.join(root, filename))
                return
        print("File not found.")
    except Exception as e:
        print(f"Error searching for file '{filename}' in directory '{directory}': {e}")

def show_file_contents(file_path):
    """Show the contents of a file."""
    try:
        with open(file_path, 'r') as f:
            contents = f.read()
        print("File contents:\n", contents)
    except Exception as e:
        print(f"Error showing contents of file '{file_path}': {e}")

def rename_multiple_files(directory, old_char, new_char, recursive):
    """Rename all the files and folders in a directory."""
    try:
        if recursive:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    new_file = file.replace(old_char, new_char)
                    os.rename(os.path.join(root, file), os.path.join(root, new_file))
                for dir in dirs:
                    new_dir = dir.replace(old_char, new_char)
                    os.rename(os.path.join(root, dir), os.path.join(root, new_dir))
        else:
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                new_item = item.replace(old_char, new_char)
                os.rename(item_path, os.path.join(directory, new_item))
        print("Files and folders renamed successfully.")
    except Exception as e:
        print(f"Error renaming files in directory '{directory}': {e}")

def main():
    parser = argparse.ArgumentParser(description="File management script.")
    parser.add_argument('action', choices=['create', 'delete', 'move', 'copy', 'rename', 'list', 'search', 'show', 'rename_multiple'], help="Action to perform")
    parser.add_argument('--src', help="Source file path")
    parser.add_argument('--dst', help="Destination file path")
    parser.add_argument('--directory', help="Directory path")
    parser.add_argument('--filename', help="Filename to search for")
    parser.add_argument('--old_char', help="Character to replace")
    parser.add_argument('--new_char', help="New character")
    parser.add_argument('--recursive', action='store_true', help="Rename files and folders recursively")

    args = parser.parse_args()

    if args.action == 'create' and args.src:
        create_file(args.src)
    elif args.action == 'delete' and args.src:
        delete_file(args.src)
    elif args.action == 'move' and args.src and args.dst:
        move_file(args.src, args.dst)
    elif args.action == 'copy' and args.src and args.dst:
        copy_file(args.src, args.dst)
    elif args.action == 'rename' and args.src and args.dst:
        rename_file(args.src, args.dst)
    elif args.action == 'list' and args.directory:
        list_files(args.directory)
    elif args.action == 'search' and args.directory and args.filename:
        search_files(args.directory, args.filename)
    elif args.action == 'show' and args.src:
        show_file_contents(args.src)
    elif args.action == 'rename_multiple' and args.directory and args.old_char and args.new_char:
        rename_multiple_files(args.directory, args.old_char, args.new_char, args.recursive)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
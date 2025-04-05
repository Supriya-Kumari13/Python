import os

def list_directory_contents(path):
    try:
        # List all files and directories in the given path
        contents = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")

if __name__ == "__main__":
    # Specify the directory path (current directory in this case)
    directory_path = os.getcwd()
    list_directory_contents(directory_path)
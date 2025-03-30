import os

# Get the list of files and directories in the current directory
directory_content = os.listdir()

# Print the content of the directory
print("Content of the directory:")
for item in directory_content:
    print(item)
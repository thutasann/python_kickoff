import os


def read_file(file_path):

    if not os.path.exists(file_path):
        return f"The file at path '{file_path}' was not found."

    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "The file was not found."
    except IOError:
        return "An error occurred while reading the file."


file_path = "example.txt"
print(f"Checking for file at: {os.path.abspath(file_path)}")
content = read_file(file_path)
print(content)

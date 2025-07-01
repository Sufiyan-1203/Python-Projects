import os

def generate_tree(path, prefix=""):
    if not os.path.exists(path):
        print("Path does not exist.")
        return

    files = sorted(os.listdir(path))
    pointers = ['├── '] * (len(files) - 1) + ['└── ']

    for pointer, file in zip(pointers, files):
        file_path = os.path.join(path, file)
        print(prefix + pointer + file)

        if os.path.isdir(file_path):
            extension = '│   ' if pointer == '├── ' else '    '
            generate_tree(file_path, prefix + extension)

path_input = input("Enter the directory path: ")
generate_tree(path_input)

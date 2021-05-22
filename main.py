from pathlib import Path
from converter import format_bytes
import os

input_folder = input("Enter the desired path: ")

dirs_to_exclude = ['.git', 'node_modules']

for root, dirs, files in os.walk(input_folder):
    # Exclude directories
    for item in dirs_to_exclude:
        if item in dirs:
            dirs.remove(item)
    for file in files:
        item = os.path.join(root, file)
        item_size = os.stat(item).st_size
        print(format_bytes(item_size))
        print(item)
        print(file)

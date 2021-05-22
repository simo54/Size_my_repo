from pathlib import Path
from converter import format_bytes
import os

input_folder = input("Enter the desired path: ")
# target_folder = Path(input_folder)

# list_files = os.listdir(target_folder)

# for item in list_files:
#     print(item)
#     print(os.stat(item).st_size)
#     # file_size = os.path.getsize(item)

for root, dirs, files in os.walk(os.path.abspath(input_folder)):
    for file in files:
        item = os.path.join(root, file)
        item_size = os.stat(item).st_size
        print(format_bytes(item_size))
        print(item)

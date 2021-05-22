import os

from openpyxl import Workbook, load_workbook
from pathlib import Path
from converter import format_bytes

workbook = Workbook()
page = workbook.active
column_name = [["File_Name", "Path", "Size", "Label"]]

input_folder = input("\n👋 Howdy? Enter the desired path: ")

question = input("\n❌ Do you want to exclude any folders? yes/no: ")

if question == "yes":
    input_dirs = input("\nWrite the repos (space for separation): ")
    dirs_to_exclude = input_dirs.split()

for col_name in column_name:
    page.append(col_name)

print("\n⏱  Loaders are expensive but trust me, I am working ^_____^")


for root, dirs, files in os.walk(input_folder):
    if 'dirs_to_exclude' in globals():
        for item in dirs_to_exclude:
            if item in dirs:
                dirs.remove(item)
    else:
        pass
    for file in files:
        item = os.path.join(root, file)
        item_size = os.stat(item).st_size
        format = format_bytes(item_size)
        format_number = format[0]
        format_label = format[1]
        page.append([file, item, format_number, format_label])

print("\n✔  All done, you see? ✔")

workbook.save(filename="result.xlsx")

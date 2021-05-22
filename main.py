import os
from openpyxl import Workbook, load_workbook
from pathlib import Path
from converter import format_bytes

workbook = Workbook()
page = workbook.active

input_folder = input("Enter the desired path: ")

question = input("Do you want to exclude any folders? yes/no: ")

if question == "yes":
    dirs_to_exclude = ['.git', 'node_modules']

column_name = [["File_Name", "Path", "Size", "Label"]]

for col_name in column_name:
    page.append(col_name)

for root, dirs, files in os.walk(input_folder):
    # Exclude directories
    if "dirs_to_exclude" in globals():
        for item in dirs_to_exclude:
            if item in dirs:
                dirs.remove(item)
    for file in files:
        item = os.path.join(root, file)
        item_size = os.stat(item).st_size
        format = format_bytes(item_size)
        format_number = format[0]
        format_label = format[1]
        page.append([file, item, format_number, format_label])

workbook.save(filename="result.xlsx")

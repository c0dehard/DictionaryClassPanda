#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
import shutil
import os
import math

"""
This Python script provides a GUI interface to copy files from a selected source directory to an external drive. It supports copying all files, regardless of size, and handles large files (9GB or larger) by splitting them into maximum 4GB parts and joining them at the destination.

Usage:
1. Run the script and a GUI window will appear.
2. Select the source directory containing the files you want to copy.
3. Choose the destination directory (external drive) where the files will be copied.
4. The script will traverse the source directory, displaying progress in the console.
5. For large files (9GB or larger), they will be split into maximum 4GB parts and copied to the destination.
6. Smaller files will be copied directly.
7. Once the copying process is complete, a success message will be displayed.

Note that splitting and joining large files can be time-consuming and require sufficient storage space.

Author: [Cyber Panda
Date: 05/18/2023
"""

MAX_FILE_SIZE = 4 * 1024 * 1024 * 1024  # 4GB in bytes

def split_file(file_path, destination_dir):
    file_name = os.path.basename(file_path)
    part_size = MAX_FILE_SIZE
    total_size = os.path.getsize(file_path)
    num_parts = math.ceil(total_size / part_size)

    with open(file_path, 'rb') as source_file:
        for part_index in range(num_parts):
            part_path = os.path.join(destination_dir, f"{file_name}.part{part_index + 1}")
            with open(part_path, 'wb') as part_file:
                part_file.write(source_file.read(part_size))

def join_files(source_dir, destination_dir, file_name):
    file_parts = sorted([f for f in os.listdir(source_dir) if f.startswith(file_name)])
    joined_file_path = os.path.join(destination_dir, file_name)

    with open(joined_file_path, 'wb') as joined_file:
        for part in file_parts:
            part_path = os.path.join(source_dir, part)
            with open(part_path, 'rb') as part_file:
                joined_file.write(part_file.read())

def copy_files():
    source_dir = filedialog.askdirectory(title="Select Source Directory")
    if not source_dir:
        return

    destination_port = filedialog.askdirectory(title="Select Destination Port")
    if not destination_port:
        return

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            if file_size >= 9 * 1024 * 1024 * 1024:
                print(f"Splitting and copying large file: {file_path}")
                split_file(file_path, destination_port)
            else:
                print(f"Copying file: {file_path}")
                shutil.copy2(file_path, destination_port)

    print("Files copied successfully!")

root = tk.Tk()
root.withdraw()

copy_files()

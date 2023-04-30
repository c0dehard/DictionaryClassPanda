import os
import shutil

"""
This Python script prompts the user to input a directory path and a file extension (or no extension for all files),
then moves all files with that extension (or all files if no extension is provided) from the subdirectories of the
input path to a new directory specified by the user.

The script utilizes the os and shutil modules to navigate and move files within the file system.
"""


# Prompt the user to input the destination directory path
dest_dir = input("Enter the destination directory path: ")

# Prompt the user to input the file extension(s) of the files they want to move
extensions = input("Enter file extension(s) (comma-separated): ").split(',')

# Loop through the extensions and remove any leading/trailing whitespace
extensions = [ext.strip() for ext in extensions]

# Check if the destination directory path is valid
if not os.path.isdir(dest_dir):
    print("Error: Invalid directory path.")
else:
    # Loop through all subdirectories
    for root, dirs, files in os.walk('.'):
        for filename in files:
            # Check if the file's extension is in the list of extensions
            if os.path.splitext(filename)[1].strip('.') in extensions or not extensions:
                # Construct the source and destination paths
                src_path = os.path.join(root, filename)
                dest_path = os.path.join(dest_dir, filename)
                # Move the file to the destination directory
                shutil.move(src_path, dest_path)

    print(f"All {' '.join(extensions) if extensions else 'files'} have been moved to {dest_dir}")

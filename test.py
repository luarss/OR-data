import os
import shutil

def copy_md_files(source_folder, destination_folder):
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith('.md'):
                source_path = os.path.join(foldername, filename)
                destination_path = os.path.join(destination_folder, filename)

                # Check if the file already exists in the destination folder
                counter = 1
                while os.path.exists(destination_path):
                    # If file exists, append a number to the filename
                    base_name, ext = os.path.splitext(filename)
                    new_filename = f"{base_name}_{counter}{ext}"
                    destination_path = os.path.join(destination_folder, new_filename)
                    counter += 1

                # Copy the file to the destination folder
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {source_path} to {destination_path}")

# Example usage:
source_folder = "../OpenROAD"
destination_folder = "."

copy_md_files(source_folder, destination_folder)


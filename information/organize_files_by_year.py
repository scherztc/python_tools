import os
import shutil
from datetime import datetime

def organize_files_by_year(source_folder, destination_root):
    if not os.path.exists(source_folder):
        print(f"Source folder does not exist: {source_folder}")
        return

    os.makedirs(destination_root, exist_ok=True)

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Skip non-files
        if not os.path.isfile(source_path):
            continue

        mod_time = os.path.getmtime(source_path)
        year = datetime.fromtimestamp(mod_time).year
        file_size = os.path.getsize(source_path)

        year_folder = os.path.join(destination_root, str(year))
        os.makedirs(year_folder, exist_ok=True)

        # Check if any file in the destination year folder has the same size
        size_match_found = False
        for existing_file in os.listdir(year_folder):
            existing_path = os.path.join(year_folder, existing_file)
            if os.path.isfile(existing_path) and os.path.getsize(existing_path) == file_size:
                size_match_found = True
                break

        if size_match_found:
            print(f"Skipped {filename} (a file with same size exists in {year_folder})")
            continue

        dest_path = os.path.join(year_folder, filename)
        print(f"Moving {filename} to {year_folder}")
        shutil.move(source_path, dest_path)

if __name__ == "__main__":
    source_dir = input("Enter the path of the folder to organize: ")
    destination_dir = input("Enter the destination root folder: ")
    organize_files_by_year(source_dir, destination_dir)


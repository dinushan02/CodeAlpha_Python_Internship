import os
import shutil

source_folder = "source_folder"
destination_folder = "jpg_images"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

if os.path.exists(source_folder):
    files = os.listdir(source_folder)

    moved_count = 0

    for file in files:
        if file.endswith(".jpg"):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)

            shutil.move(source_path, destination_path)
            moved_count += 1

    if moved_count > 0:
        print(f"{moved_count} JPG file(s) moved successfully to '{destination_folder}'.")
    else:
        print("No JPG files found in the source folder.")
else:
    print("Source folder not found!")
import os
import shutil

source_folder = "Photos"
target_folder = "sorted_photos"

# create the new folder if it does not exist
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

moved_count = 0

for filename in os.listdir(source_folder):
    if filename.lower().endswith((".jpg", ".jpeg")):
        old_path = os.path.join(source_folder, filename)
        new_path = os.path.join(target_folder, filename)
        shutil.move(old_path, new_path)
        print("Moved:", filename)
        moved_count = moved_count + 1

if moved_count == 0:
    print("No jpg files found.")
else:
    print("Done! Moved", moved_count, "files.")
CodeAlpha_TaskAutomation

A simple photo organizer script made with Python.

About
Messy folders waste time. This script automates a boring, repetitive job: it looks through the `Photos` folder, finds all `.jpg` files and moves them into a new folder called `sorted_photos`. Other files, like text notes, are left where they are.

Features
- Creates the `sorted_photos` folder automatically if it does not exist
- Finds .jpg and .jpeg files, even if the extension is in capital letters
- Moves only the photos and leaves other files alone
- Prints each file name as it is moved
- Shows how many files were moved, or a message if none were found

Concepts used
- `os` module (list files, join paths, create folders)
- `shutil` module (move files)
- `for` loop
- `if-else` statements
- String methods (`lower`, `endswith`)

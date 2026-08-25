# CodeAlpha File Organizer

## 📌 Project Overview

This project is a simple file automation program developed using Python as part of the CodeAlpha Python Programming Internship.

The program automatically identifies `.jpg` image files from a source folder and moves them into a separate `jpg_images` folder.

This project demonstrates how Python can be used to automate repetitive file management tasks.

## 🎯 Features

- Automatically checks the source folder for files.
- Identifies files with the `.jpg` extension.
- Automatically creates the `jpg_images` folder if it does not exist.
- Moves JPG files from the source folder to the destination folder.
- Counts the number of JPG files moved.
- Leaves non-JPG files untouched.
- Handles cases where no JPG files are found.
- Handles cases where the source folder does not exist.
- Displays a clear result message.

## 🛠️ Technologies Used

- Python
- `os` module
- `shutil` module

## 🧠 Python Concepts Used

- Variables
- Strings
- `if-else` statements
- `for` loop
- Lists
- File and folder handling
- `os.path.exists()`
- `os.makedirs()`
- `os.listdir()`
- `os.path.join()`
- `str.endswith()`
- `shutil.move()`
- Counters
- Conditional logic

## ⚙️ How the Program Works

1. The program defines the source folder and destination folder.
2. It checks whether the destination folder exists.
3. If the destination folder does not exist, Python creates it automatically.
4. The program checks whether the source folder exists.
5. It gets the list of files inside the source folder.
6. It checks each file to determine whether it ends with `.jpg`.
7. If the file is a JPG image, its source and destination paths are created.
8. The JPG file is moved to the `jpg_images` folder.
9. The program counts how many JPG files were moved.
10. A message is displayed showing the result.

## 🧪 Example

### Before Running the Program

```text
source_folder/
├── automation_notes.txt
├── photo1.jpg
├── photo2.jpg
├── photo3.jpg
└── Python.pdf
```

### After Running the Program

```text
source_folder/
├── automation_notes.txt
└── Python.pdf

jpg_images/
├── photo1.jpg
├── photo2.jpg
└── photo3.jpg
```

The program moves only the `.jpg` files while leaving the other file types untouched.

## 🖥️ Example Output

When JPG files are found:

```text
3 JPG file(s) moved successfully to 'jpg_images'.
```

When no JPG files are found:

```text
No JPG files found in the source folder.
```

When the source folder does not exist:

```text
Source folder not found!
```

## ▶️ How to Run

Make sure Python is installed on your computer.

Place the required files inside the `source_folder` directory.

Run the following command:

```bash
python file_organizer.py
```

The program will automatically organize the JPG files into the `jpg_images` folder.

## 📁 Project Structure

```text
Task_3_Task_Automation/
│
├── source_folder/
│   ├── automation_notes.txt
│   ├── photo1.jpg
│   ├── photo2.jpg
│   ├── photo3.jpg
│   └── Python.pdf
│
├── file_organizer.py
└── README.md
```

After running the program, the `jpg_images` folder will be created automatically:

```text
Task_3_Task_Automation/
│
├── source_folder/
│   ├── automation_notes.txt
│   └── Python.pdf
│
├── jpg_images/
│   ├── photo1.jpg
│   ├── photo2.jpg
│   └── photo3.jpg
│
├── file_organizer.py
└── README.md
```

## 👨‍💻 Author
M. Dinushan
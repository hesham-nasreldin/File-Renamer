# File Renamer

A simple Python script that renames all files in a specified folder with sequential numbering (e.g., 01.jpg, 02.jpg, etc.).

## Features

- Renames files in a folder with zero-padded two-digit numbers
- Starts numbering from a specified number (default: 1)
- Preserves file extensions
- Handles errors gracefully

## Requirements

- Python 3.x

## Usage

1. Place the files you want to rename in a folder (default: `./test_files`)
2. Run the script:

```bash
python main.py
```

You can modify the `target_folder` variable in the script to point to a different folder.

## Example

Before:
- image1.jpg
- photo.png
- document.pdf

After:
- 01.jpg
- 02.png
- 03.pdf

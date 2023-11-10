## Artemis

**Artemis** is a Python script that automates file categorization and organization based on file extensions


## Table of Contents

- [About](#about)
- [Features](#features)
- [Usage](#usage)
- [File Categories](#file-categories)

## About

**Artemis** is a Python script designed to simplify the task of organizing files in a directory by categorizing them into different folders based on their file extensions. It aims to help you maintain a more organized and structured file system, making it easier to find and manage your files.

## Features

- Automatically categorizes files into various predefined categories, such as Documents, Images, Audio, Video, Code, and more.
- Supports a wide range of file extensions, ensuring that most common file types are appropriately sorted.
- Provides a flexible "Other" category for any file extensions not explicitly listed in the predefined categories.
- Simple and easy-to-use command-line interface, allowing you to organize your files with just a few simple steps.

## Usage

1. Clone this repository to your local machine:

    ```bash
    git clone [https://github.com/Aadhav-VijayaSaravanan/file-organizer.git](https://github.com/Aadhav-VijayaSaravanan/file-organizer.git)
    ```

   OR download a zip file of the project using the "Download ZIP" button on the GitHub page.

2. Navigate to the cloned directory:

    ```bash
    cd file-organizer
    ```

3. Run the script by providing the path to the directory you want to organize:

    ```bash
    python file_organizer.py
    ```

4. Follow the on-screen instructions to input the path, and the script will organize the files accordingly.

## File Categories

The script organizes files into the following categories:

1. Documents:
   - .pdf, .docx, .txt, .pptx, .doc, .xls, .csv, .odt

2. Images:
   - .png, .jpg, .jpeg, .gif, .bmp, .tiff, .eps

3. Audio:
   - .m4a, .mp3, .wav, .flac, .aac, .ogg, .wma

4. Video:
   - .mp4, .avi, .mkv, .wmv, .flv, .mov

5. Code:
   - .py, .java, .cpp, .html, .css, .js, .json, .sql, .php

6. Archives:
   - .zip, .rar, .7z, .tar, .gz

7. Other: Files with extensions not listed in the categories above

Make sure to provide a valid path to the directory you want to organize, and the script will move the files to their respective folders according to their extensions.

Enjoy your organized files!

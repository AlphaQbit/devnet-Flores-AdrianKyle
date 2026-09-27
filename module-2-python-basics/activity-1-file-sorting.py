"""
Module 2 — Activity: File Sorting with os and shutil
Student: Adrian Kyle Flores
Date: 9/27/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
i built a simple file sorting program that checks the files inside
a folder and moves them into different folders based on their file
extension this makes it easier to organize files automatically


============================================
KEY VOCABULARY
============================================
- os module: used to work with folders files and file paths
- shutil module: used to move and manage files
- file path: the location of a file on the computer
- directory: another name for a folder
- extension: the part of a file name that tells what type of file it is


============================================
YOUR SCRIPT
============================================
"""

import os
import shutil

folder = input("enter the folder path: ")

if os.path.exists(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file)[1].lower()

            if extension:
                folder_name = extension[1:].upper() + " Files"
                new_folder = os.path.join(folder, folder_name)

                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)

                shutil.move(file_path, os.path.join(new_folder, file))

    print("files sorted successfully")
else:
    print("folder does not exist")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
i can make mistakes with file paths because the folder needs to exist
before the program can work i also need to be careful when moving files
so i dont accidentally move something to the wrong folder


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
this connects to automation because the program can organize files
without me having to move every file manually something like this could
also help organize school files like documents images and assignments
"""

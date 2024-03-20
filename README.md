# Open In Blender

Are you tired of opening blender and the navigating the import menus to get an FBX into your scene? Well, friend, you're in luck.

This repository contains a batch file and a Python script designed to streamline the process of opening files that blender can technically import (such as `.fbx`, `.obj`, or `.dae`) but are not supported for directly opening with the main blender exe.

## How it works

The `open_in_blender.bat` batch file calls Blender with the `import_model.py`script as an argument. The Python script then deletes all objects in the default scene and imports the selected file.

## Prerequisites

- Blender 3.x installed on your system.
- Windows operating system (the batch file is designed for Windows).

## Installation

1. Clone or download this repository to your local machine.
2. Ensure that the path to Blender in `open_in_blender.bat` matches your Blender installation path. If your Blender is installed in a different location than the default, edit the `.bat` file with a text editor and modify the path accordingly.
3. You can place the scripts wherever you like, as long as you make sure to keep the two scripts in the same folder.

## Usage

1. Right-click on an `.fbx`, `.obj`, or `.dae` file in Windows Explorer.
2. Select `Open with > Choose another app > More apps > Look for another app on this PC`.
3. Navigate to the directory where you cloned this repository and select the `open_with_blender.bat` file.
4. Click the checkbox to set it as the default way to open these files.
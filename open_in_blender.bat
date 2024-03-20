@echo off

:: NOTE: If you have blender installed in a non-standard location be sure to change this!
set BLENDER_PATH="C:\Program Files\Blender Foundation\Blender 3.4\blender.exe"

%BLENDER_PATH% --python "%~dp0import_model.py" -- %1
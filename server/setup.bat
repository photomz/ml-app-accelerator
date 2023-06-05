@echo off
REM This is a batch script for setting up the environment

REM Check if pip is installed
where pip >nul 2>nul
if %errorlevel% neq 0 (
    echo Pip not found. Please install Python which includes pip.
    pause
    exit /b
)

REM Install Python packages using pip
pip install annoy flask

REM Download a file using PowerShell's Invoke-WebRequest
powershell -Command "Invoke-WebRequest -Uri https://huggingface.co/stanfordnlp/glove/resolve/main/glove.6B.zip -OutFile glove.6B.zip"

REM Create directories if they do not exist
if not exist "data\glove" mkdir data\glove

REM Unzip downloaded file to the specified directory using PowerShell's Expand-Archive
powershell -Command "Expand-Archive -Path .\glove.6B.zip -DestinationPath .\data\glove\ -Force"

REM Cleanup and delete the ZIP
DEL .\glove.6B.zip
@echo off
REM Navigate to project directory
cd WeBeGymin

REM Create main app file
echo. > app.py

REM Create main app folder and subfolders
mkdir app
mkdir app\templates
mkdir app\static
mkdir app\models
mkdir app\routes
mkdir app\auth

REM Create __init__.py files
echo. > app\__init__.py
echo. > app\models\__init__.py
echo. > app\routes\__init__.py
echo. > app\auth\__init__.py

echo Project structure created successfully.

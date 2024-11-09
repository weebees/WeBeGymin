@echo off
REM Initialize virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

echo Project setup complete. Virtual environment activated.

# aws-tutorial

Small project. Instructions to create and use the Python virtual environment used during development.

## Create the virtual environment

From the project root (Windows PowerShell):

```powershell
python -m venv .venv
```

## Activate the virtual environment

PowerShell (recommended):

```powershell
.\.venv\Scripts\Activate.ps1
```

Command Prompt (cmd.exe):

```cmd
.venv\Scripts\activate.bat
```

macOS / Linux (bash/zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install dependencies

```powershell
.venv\Scripts\python -m pip install -r requirements.txt
```

Optionally upgrade pip:

```powershell
.venv\Scripts\python -m pip install --upgrade pip
```

## Run the app

```powershell
.venv\Scripts\python app.py
```

The app listens on port 8000 by default in development.

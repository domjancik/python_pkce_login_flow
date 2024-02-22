This repo contains a reference python implementation for handling a PKCE sign in flow. 

# Usage

### TLDR: Running a PKCE Sign-In Flow Flask App

1. **Create a Virtual Environment**: `python3 -m venv venv` (Unix) or `python -m venv venv` (Windows)
2. **Activate the Virtual Environment**: `source venv/bin/activate` (Unix) or `venv\Scripts\activate` (Windows CMD/PowerShell)
3. **Install Dependencies**: `pip install -r requirements.txt`
4. **Run the Flask App**: `python app_full_login.py`
5. **Initiate Login Flow**: Visit `http://localhost:3000/login` in your browser.

### 1. Create a Virtual Environment

A virtual environment is an isolated environment for Python projects. This allows you to manage dependencies for different projects separately. To create a virtual environment, navigate to your project's directory in the terminal and run:

```bash
# For Unix-like operating systems
python3 -m venv venv

# For Windows
python -m venv venv
```

This command creates a virtual environment named `venv` in your project directory.

### 2. Activate the Virtual Environment

Before you install dependencies, you need to activate the virtual environment. Depending on your operating system, you can activate it by running one of the following commands in your terminal:

```bash
# For Unix-like operating systems
source venv/bin/activate

# For Windows (cmd.exe)
venv\Scripts\activate.bat

# For Windows (PowerShell)
venv\Scripts\Activate.ps1
```

### 3. Install Requirements

Your project should have a `requirements.txt` file listing all necessary Python packages. Install these packages by running:

```bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file and installs all listed packages in your activated virtual environment.

### 4. Run Full Login Flow Flask App

With your virtual environment activated and all dependencies installed, you're now ready to run the Flask application that implements the PKCE sign-in flow.

To start the Flask application, simply execute the following command in your terminal:

```bash
python app_full_login.py
```

### 5. Start the Login Flow

After starting the Flask app, you can initiate the login flow by opening a web browser and navigating to `http://localhost:3000/login`. This URL triggers the PKCE sign-in flow defined in your Flask application.
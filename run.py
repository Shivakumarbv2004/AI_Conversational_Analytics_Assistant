import subprocess
import sys
import time
import os

def get_python_executable():
    # Check if a .venv exists in the current directory
    venv_path = os.path.join(os.path.dirname(__file__), ".venv")
    if os.path.exists(venv_path):
        if os.name == 'nt':
            return os.path.join(venv_path, "Scripts", "python.exe")
        else:
            return os.path.join(venv_path, "bin", "python")
    return sys.executable

def main():
    print("Starting AI Conversational Analytics Assistant...")

    # Set python path to current directory so 'app' module can be found
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.abspath(os.path.dirname(__file__))
    
    python_exe = get_python_executable()
    print(f"Using Python executable: {python_exe}")

    # Start FastAPI backend
    backend_process = subprocess.Popen(
        [python_exe, "-m", "uvicorn", "app.api.main:app", "--host", "127.0.0.1", "--port", "8000"],
        env=env
    )
    
    print("Backend started on http://127.0.0.1:8000")
    
    # Wait a bit for backend to start
    time.sleep(2)
    
    # Start Streamlit frontend
    frontend_process = subprocess.Popen(
        [python_exe, "-m", "streamlit", "run", "frontend/streamlit_app.py"],
        env=env
    )
    
    print("Frontend started. Opening in browser...")
    
    try:
        # Keep the main process running
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\nShutting down processes...")
        backend_process.terminate()
        frontend_process.terminate()
        backend_process.wait()
        frontend_process.wait()
        print("Shutdown complete.")

if __name__ == "__main__":
    main()

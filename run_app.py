#!/usr/bin/env python3
"""
Launcher script for the Call Schedule Generator application.
This script checks dependencies and launches the main application.
"""

import sys
import subprocess
import importlib.util

def check_dependency(module_name, package_name=None):
    """Check if a module is available, install if needed"""
    if package_name is None:
        package_name = module_name
    
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        print(f"Installing {package_name}...")
        try:
            # Try with --user flag first for externally managed environments
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package_name])
            print(f"Successfully installed {package_name}")
            return True
        except subprocess.CalledProcessError:
            try:
                # Fallback to regular install
                subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
                print(f"Successfully installed {package_name}")
                return True
            except subprocess.CalledProcessError:
                print(f"Failed to install {package_name}")
                return False
    return True

def main():
    print("Call Schedule Generator")
    print("=" * 30)
    
    # Check and install dependencies
    print("Checking dependencies...")
    
    dependencies = [
        ("openpyxl", "openpyxl"),
        ("tkcalendar", "tkcalendar")
    ]
    
    all_installed = True
    for module, package in dependencies:
        if not check_dependency(module, package):
            all_installed = False
    
    if not all_installed:
        print("Some dependencies could not be installed. Please install them manually:")
        print("pip install -r requirements.txt")
        input("Press Enter to exit...")
        return
    
    print("All dependencies are available!")
    print("Starting application...")
    print()
    
    # Import and run the main application
    try:
        from call_scheduler import main as run_app
        run_app()
    except ImportError as e:
        print(f"Error importing application: {e}")
        print("Make sure call_scheduler.py is in the same directory as this script.")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"Error running application: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main() 
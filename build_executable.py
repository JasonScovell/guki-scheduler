#!/usr/bin/env python3
"""
Build script to create standalone executable for Call Schedule Generator
Works on both Mac and Windows
"""

import os
import sys
import subprocess
import platform

def main():
    print("Call Schedule Generator - Executable Builder")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('call_scheduler_optimized.py'):
        print("❌ Error: call_scheduler_optimized.py not found!")
        print("Please run this script from the project directory.")
        return
    
    # Install PyInstaller if not already installed
    print("📦 Installing PyInstaller...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'pyinstaller'], 
                      check=True, capture_output=True)
        print("✅ PyInstaller installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install PyInstaller: {e}")
        return
    
    # Determine OS and set appropriate options
    system = platform.system()
    print(f"🖥️  Detected OS: {system}")
    
    if system == "Darwin":  # macOS
        print("🍎 Building for macOS...")
        icon_option = []
        # macOS specific options - build both executable and app bundle
        extra_options = [
            '--onefile',   # Single executable
            '--name=CallScheduleGenerator',
            '--add-data=requirements.txt:.',
            '--hidden-import=tkinter',
            '--hidden-import=tkinter.ttk',
            '--hidden-import=tkinter.messagebox',
            '--hidden-import=openpyxl',
            '--hidden-import=sqlite3',
            '--hidden-import=datetime',
            '--hidden-import=calendar',
            '--hidden-import=threading',
            '--hidden-import=queue',
            '--hidden-import=random',
            '--hidden-import=os',
            '--hidden-import=sys',
            '--hidden-import=json',
            '--hidden-import=pathlib',
            '--collect-all=tkinter',
            '--collect-all=openpyxl'
        ]
    elif system == "Windows":
        print("🪟 Building for Windows...")
        icon_option = []
        # Windows specific options
        extra_options = [
            '--windowed',  # No console window
            '--onefile',   # Single executable
            '--name=CallScheduleGenerator',
            '--add-data=requirements.txt;.',
            '--hidden-import=tkinter',
            '--hidden-import=tkinter.ttk',
            '--hidden-import=tkinter.messagebox',
            '--hidden-import=openpyxl',
            '--hidden-import=sqlite3',
            '--hidden-import=datetime',
            '--hidden-import=calendar',
            '--hidden-import=threading',
            '--hidden-import=queue',
            '--hidden-import=random',
            '--hidden-import=os',
            '--hidden-import=sys',
            '--hidden-import=json',
            '--hidden-import=pathlib'
        ]
    else:
        print(f"❌ Unsupported OS: {system}")
        print("This script supports macOS and Windows only.")
        return
    
    # Build command
    cmd = [sys.executable, '-m', 'PyInstaller'] + extra_options + ['call_scheduler_optimized.py']
    
    print("🔨 Building executable...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ Build completed successfully!")
        
        # Show output location
        if system == "Darwin":
            exe_path = "dist/CallScheduleGenerator"
            print(f"📁 Executable created at: {exe_path}")
        else:
            exe_path = "dist/CallScheduleGenerator.exe"
            print(f"📁 Executable created at: {exe_path}")
        
        print("\n📋 Next steps:")
        print("1. Test the executable by running it")
        print("2. Create a zip file with the executable")
        print("3. Share the zip file with others")
        
        # Create a simple launcher script
        create_launcher_script(system)
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed!")
        print(f"Error: {e}")
        print(f"Output: {e.stdout}")
        print(f"Error: {e.stderr}")

def create_launcher_script(system):
    """Create a simple launcher script for easier distribution"""
    if system == "Darwin":
        launcher_content = """#!/bin/bash
# Call Schedule Generator Launcher for macOS
echo "Starting Call Schedule Generator..."
./CallScheduleGenerator
"""
        with open('launch_mac.sh', 'w') as f:
            f.write(launcher_content)
        os.chmod('launch_mac.sh', 0o755)
        print("📝 Created launcher script: launch_mac.sh")
        
    elif system == "Windows":
        launcher_content = """@echo off
REM Call Schedule Generator Launcher for Windows
echo Starting Call Schedule Generator...
CallScheduleGenerator.exe
pause
"""
        with open('launch_windows.bat', 'w') as f:
            f.write(launcher_content)
        print("📝 Created launcher script: launch_windows.bat")

if __name__ == "__main__":
    main() 
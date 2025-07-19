#!/usr/bin/env python3
"""
Build macOS app bundle for Call Schedule Generator
"""

import os
import sys
import subprocess
import platform
import shutil

def main():
    print("🍎 macOS App Bundle Builder")
    print("=" * 40)
    
    if platform.system() != "Darwin":
        print("❌ This script is for macOS only!")
        return
    
    # Check if we're in the right directory
    if not os.path.exists('call_scheduler_optimized.py'):
        print("❌ Error: call_scheduler_optimized.py not found!")
        return
    
    # Clean up previous builds
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')
    
    print("🔨 Building macOS app bundle...")
    
    # Build command for app bundle
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--windowed',  # Create app bundle (no console)
        '--onedir',    # Directory mode (not onefile for app bundle)
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
        '--collect-all=openpyxl',
        '--clean',
        'call_scheduler_optimized.py'
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ App bundle built successfully!")
        
        # Check if app bundle was created
        app_path = "dist/CallScheduleGenerator.app"
        if os.path.exists(app_path):
            print(f"📱 App bundle created at: {app_path}")
            
            # Make it executable
            os.chmod(f"{app_path}/Contents/MacOS/CallScheduleGenerator", 0o755)
            print("✅ Made app bundle executable")
            
            # Create a simple launcher script
            create_app_launcher()
            
        else:
            print("❌ App bundle not found!")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed!")
        print(f"Error: {e}")
        print(f"Output: {e.stdout}")
        print(f"Error: {e.stderr}")

def create_app_launcher():
    """Create a launcher script for the app bundle"""
    launcher_content = """#!/bin/bash
# Call Schedule Generator App Launcher
echo "Starting Call Schedule Generator..."
open "dist/CallScheduleGenerator.app"
"""
    
    with open('launch_app.sh', 'w') as f:
        f.write(launcher_content)
    os.chmod('launch_app.sh', 0o755)
    print("📝 Created app launcher: launch_app.sh")

if __name__ == "__main__":
    main() 
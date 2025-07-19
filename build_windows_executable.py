#!/usr/bin/env python3
"""
Build Windows executable for Call Schedule Generator
"""

import os
import sys
import subprocess
import platform

def main():
    print("🪟 Windows Executable Builder")
    print("=" * 40)
    
    if platform.system() != "Darwin":
        print("❌ This script is for macOS only!")
        print("On Windows, use: python build_executable.py")
        return
    
    # Check if we're in the right directory
    if not os.path.exists('call_scheduler_optimized.py'):
        print("❌ Error: call_scheduler_optimized.py not found!")
        return
    
    print("🔨 Building Windows executable...")
    print("Note: This creates a Windows-compatible executable from macOS")
    
    # Build command for Windows executable
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',   # Single executable
        '--name=GUKI_Scheduler_Windows',
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
        '--hidden-import=pathlib',
        '--collect-all=tkinter',
        '--collect-all=openpyxl',
        '--target-arch=x86_64',  # 64-bit Windows
        '--distpath=windows_build',
        'call_scheduler_optimized.py'
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ Windows executable built successfully!")
        
        # Check if executable was created
        exe_path = "windows_build/GUKI_Scheduler_Windows.exe"
        if os.path.exists(exe_path):
            print(f"📁 Windows executable created at: {exe_path}")
            
            # Create Windows launcher script
            create_windows_launcher()
            
        else:
            print("❌ Windows executable not found!")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed!")
        print(f"Error: {e}")
        print(f"Output: {e.stdout}")
        print(f"Error: {e.stderr}")

def create_windows_launcher():
    """Create a Windows launcher script"""
    launcher_content = """@echo off
REM GUKI Scheduler Windows Launcher
echo Starting GUKI Scheduler...
GUKI_Scheduler_Windows.exe
pause
"""
    
    with open('windows_build/launch_windows.bat', 'w') as f:
        f.write(launcher_content)
    print("📝 Created Windows launcher: windows_build/launch_windows.bat")

if __name__ == "__main__":
    main() 
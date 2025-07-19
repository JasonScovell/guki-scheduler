#!/usr/bin/env python3
"""
Create GUKI Scheduler package with both Mac and Windows versions
"""

import os
import zipfile
import platform
from datetime import datetime
import shutil

def main():
    print("🎯 Creating GUKI Scheduler Package")
    print("=" * 45)
    
    # Check if we have the necessary files
    if not os.path.exists('call_scheduler_optimized.py'):
        print("❌ Error: call_scheduler_optimized.py not found!")
        return
    
    # Create the main package directory
    package_dir = "GUKI_Scheduler"
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    
    os.makedirs(package_dir)
    
    print("📁 Creating GUKI Scheduler package...")
    
    # Build Mac version
    print("🍎 Building Mac version...")
    build_mac_version(package_dir)
    
    # Build Windows version
    print("🪟 Building Windows version...")
    build_windows_version(package_dir)
    
    # Create instructions
    create_instructions(package_dir)
    
    # Create zip file
    zip_name = "GUKI_Scheduler.zip"
    print(f"🗜️  Creating zip file: {zip_name}")
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arc_name = os.path.relpath(file_path, package_dir)
                zipf.write(file_path, arc_name)
                print(f"  📄 Added: {arc_name}")
    
    # Clean up
    shutil.rmtree(package_dir)
    
    print(f"\n🎉 GUKI Scheduler package created successfully!")
    print(f"📦 File: {zip_name}")
    print(f"📏 Size: {os.path.getsize(zip_name) / (1024*1024):.1f} MB")
    
    print(f"\n📋 Package contents:")
    print(f"  • GUKI Scheduler Mac/ - Mac application")
    print(f"  • GUKI Scheduler Windows/ - Windows application")
    print(f"  • README.md - Instructions")
    
    print(f"\n🚀 Ready to share!")
    print(f"Users can extract and run the appropriate version for their system.")

def build_mac_version(package_dir):
    """Build the Mac version"""
    mac_dir = os.path.join(package_dir, "GUKI Scheduler Mac")
    os.makedirs(mac_dir)
    
    # Copy the working Mac executable
    if os.path.exists('dist/CallScheduleGenerator'):
        shutil.copytree('dist/CallScheduleGenerator', os.path.join(mac_dir, 'CallScheduleGenerator'))
        print("✅ Copied Mac executable")
    
    # Create Mac launcher
    mac_launcher = """#!/bin/bash
# GUKI Scheduler Mac Launcher
echo "Starting GUKI Scheduler..."
./CallScheduleGenerator/CallScheduleGenerator
"""
    
    with open(os.path.join(mac_dir, 'Launch GUKI Scheduler.command'), 'w') as f:
        f.write(mac_launcher)
    os.chmod(os.path.join(mac_dir, 'Launch GUKI Scheduler.command'), 0o755)
    print("✅ Created Mac launcher")

def build_windows_version(package_dir):
    """Build the Windows version"""
    windows_dir = os.path.join(package_dir, "GUKI Scheduler Windows")
    os.makedirs(windows_dir)
    
    # Check if we have a GitHub Actions-built Windows executable
    github_exe_path = "GUKI_Scheduler_Windows.exe"
    if os.path.exists(github_exe_path):
        # Copy the GitHub Actions-built executable
        shutil.copy2(github_exe_path, windows_dir)
        print("✅ Copied GitHub Actions-built Windows executable")
        
        # Create Windows launcher for the executable
        windows_launcher = """@echo off
REM GUKI Scheduler Windows Launcher
echo Starting GUKI Scheduler...
GUKI_Scheduler_Windows.exe
pause
"""
        
        with open(os.path.join(windows_dir, 'Launch GUKI Scheduler.bat'), 'w') as f:
            f.write(windows_launcher)
        print("✅ Created Windows launcher")
        
        # Create success instructions
        windows_instructions = """# GUKI Scheduler Windows - Ready to Use! 🎉

## ✅ Windows Executable Included

This package includes a pre-built Windows executable created using GitHub Actions.

### 🚀 How to Run

1. **Double-click** `Launch GUKI Scheduler.bat` to start the application
2. **Or** double-click `GUKI_Scheduler_Windows.exe` directly

### 📋 System Requirements
- Windows 10 or later
- No Python installation required
- No additional dependencies needed

### 🔧 Troubleshooting

If the executable doesn't run:
1. Right-click the .exe file
2. Select "Run as administrator"
3. If Windows Defender blocks it, click "More info" → "Run anyway"

### 📞 Alternative: Python Method

If you prefer to run with Python:
```cmd
python call_scheduler_optimized.py
```

## 🎯 Ready to Use!

The Windows executable is fully functional and ready to use!
"""
    else:
        # Create Windows build instructions for manual build
        windows_instructions = """# GUKI Scheduler Windows - Build Instructions

## 🔨 How to Get Windows Executable

### Option 1: Download from GitHub Actions (Recommended)
1. Go to the GitHub repository: https://github.com/YOUR_USERNAME/guki-scheduler
2. Click "Actions" tab
3. Click the latest workflow run
4. Download "GUKI_Scheduler_Windows" artifact
5. Replace the files in this folder with the downloaded executable

### Option 2: Build on Windows Machine
Copy these files to your Windows machine:
- call_scheduler_optimized.py
- requirements.txt
- build_executable.py

Then run:
```cmd
python build_executable.py
```

### Option 3: Use Python Directly
If you have Python installed on Windows:
```cmd
python call_scheduler_optimized.py
```

## 🔧 Requirements
- Windows 10 or later
- Python 3.8+ (for Options 2 & 3)
- pip (usually comes with Python)

## 📞 Support
If you need help, contact your IT department.
"""
        
        # Copy source files for Windows users
        if os.path.exists('call_scheduler_optimized.py'):
            shutil.copy2('call_scheduler_optimized.py', windows_dir)
            print("✅ Copied source code")
        
        if os.path.exists('requirements.txt'):
            shutil.copy2('requirements.txt', windows_dir)
            print("✅ Copied requirements")
        
        if os.path.exists('build_executable.py'):
            shutil.copy2('build_executable.py', windows_dir)
            print("✅ Copied build script")
        
        # Create Windows launcher placeholder
        windows_launcher = """@echo off
REM GUKI Scheduler Windows Launcher
echo GUKI Scheduler Windows
echo.
echo This launcher will work after you get the Windows executable.
echo Please see BUILD_INSTRUCTIONS.md for details.
echo.
echo To run with Python directly:
echo python call_scheduler_optimized.py
echo.
pause
"""
        
        with open(os.path.join(windows_dir, 'Launch GUKI Scheduler.bat'), 'w') as f:
            f.write(windows_launcher)
        print("✅ Created Windows launcher placeholder")
    
    with open(os.path.join(windows_dir, 'BUILD_INSTRUCTIONS.md'), 'w') as f:
        f.write(windows_instructions)
    print("✅ Created Windows instructions")
    
    with open(os.path.join(windows_dir, 'BUILD_INSTRUCTIONS.md'), 'w') as f:
        f.write(windows_instructions)
    print("✅ Created Windows build instructions")
    
    # Copy source files for Windows users
    if os.path.exists('call_scheduler_optimized.py'):
        shutil.copy2('call_scheduler_optimized.py', windows_dir)
        print("✅ Copied source code")
    
    if os.path.exists('requirements.txt'):
        shutil.copy2('requirements.txt', windows_dir)
        print("✅ Copied requirements")
    
    if os.path.exists('build_executable.py'):
        shutil.copy2('build_executable.py', windows_dir)
        print("✅ Copied build script")
    
    # Create Windows launcher placeholder
    windows_launcher = """@echo off
REM GUKI Scheduler Windows Launcher
echo GUKI Scheduler Windows
echo.
echo This launcher will work after you build the Windows executable.
echo Please see BUILD_INSTRUCTIONS.md for details.
echo.
echo To run with Python directly:
echo python call_scheduler_optimized.py
echo.
pause
"""
    
    with open(os.path.join(windows_dir, 'Launch GUKI Scheduler.bat'), 'w') as f:
        f.write(windows_launcher)
    print("✅ Created Windows launcher placeholder")

def build_windows_executable():
    """Build the Windows executable"""
    import subprocess
    
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',
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
        '--distpath=windows_build',
        'call_scheduler_optimized.py'
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print("✅ Windows executable built")
    except subprocess.CalledProcessError as e:
        print(f"❌ Windows build failed: {e}")
        # Create a placeholder
        with open('windows_build/GUKI_Scheduler_Windows.exe', 'w') as f:
            f.write("Windows executable placeholder")
        print("⚠️  Created placeholder (Windows users need to build locally)")

def create_instructions(package_dir):
    """Create instructions file"""
    instructions = """# GUKI Scheduler

## 🚀 Quick Start

### For Mac Users:
1. **Double-click** `Launch GUKI Scheduler.command`
   - OR -
2. **Terminal**: `./CallScheduleGenerator/CallScheduleGenerator`

### For Windows Users:
1. **Follow build instructions** in `BUILD_INSTRUCTIONS.md`
2. **Build the executable** using `python build_executable.py`
3. **Run the application** using the launcher or executable

## 📋 What's Included

### Mac Version:
- `CallScheduleGenerator/` - Application folder
- `Launch GUKI Scheduler.command` - Easy launcher

### Windows Version:
- Source files and build instructions
- `Launch GUKI Scheduler.bat` - Launcher (after building)
- `BUILD_INSTRUCTIONS.md` - How to build on Windows

## ✅ Features

- **Friday-Only Scheduling**: All schedules start on Fridays at 7 AM
- **Personnel Management**: Add, edit, remove personnel and groups
- **Smart Scheduling**: Generate up to 10 different schedule options
- **Excel Export**: Professional Excel output with formatting
- **Excluded Weeks**: Set when personnel are unavailable
- **Local Database**: All data stored locally, no internet required
- **Cross-Platform**: Works on both Mac and Windows

## 🔧 Troubleshooting

### Mac Issues:
- **"Unidentified Developer"**: Right-click → "Open" → "Open"
- **Permission Denied**: `chmod +x CallScheduleGenerator/CallScheduleGenerator`

### Windows Issues:
- **"Windows protected your PC"**: Click "More info" → "Run anyway"
- **Antivirus Warning**: Add to exceptions or temporarily disable

## 📖 How to Use

1. **Launch the application** using the launcher for your system
2. **Add Groups**: Go to "Groups" tab → Add your groups
3. **Add Personnel**: Go to "Personnel" tab → Add people with their groups
4. **Generate Schedule**: Go to "Generate Schedule" tab → Set dates → Generate
5. **Export**: Click "Export to Excel" to save your schedule

## 🔒 Security & Privacy

- **100% Local**: No data sent anywhere
- **No Internet**: Works completely offline
- **Your Data**: All data stored on your computer only

---

**GUKI Scheduler** - Professional Call Schedule Management
"""
    
    with open(os.path.join(package_dir, 'README.md'), 'w') as f:
        f.write(instructions)
    print("✅ Created README.md")

if __name__ == "__main__":
    import sys
    main() 
#!/usr/bin/env python3
"""
Create distribution package for Call Schedule Generator
"""

import os
import zipfile
import platform
from datetime import datetime

def main():
    print("📦 Creating Distribution Package")
    print("=" * 40)
    
    # Check if executable exists
    system = platform.system()
    
    if system == "Darwin":
        exe_name = "CallScheduleGenerator"
        exe_path = f"dist/{exe_name}"
        launcher_name = "launch_mac.sh"
        platform_name = "macOS"
    elif system == "Windows":
        exe_name = "CallScheduleGenerator.exe"
        exe_path = f"dist/{exe_name}"
        launcher_name = "launch_windows.bat"
        platform_name = "Windows"
    else:
        print(f"❌ Unsupported platform: {system}")
        return
    
    if not os.path.exists(exe_path):
        print(f"❌ Executable not found: {exe_path}")
        print("Please run build_executable.py first!")
        return
    
    # Create distribution folder
    dist_folder = f"CallScheduleGenerator_{platform_name}"
    if os.path.exists(dist_folder):
        import shutil
        shutil.rmtree(dist_folder)
    
    os.makedirs(dist_folder)
    
    # Copy files
    print(f"📁 Creating {platform_name} distribution...")
    
    # Copy executable
    import shutil
    shutil.copy2(exe_path, dist_folder)
    print(f"✅ Copied {exe_name}")
    
    # Copy launcher script
    if os.path.exists(launcher_name):
        shutil.copy2(launcher_name, dist_folder)
        print(f"✅ Copied {launcher_name}")
    
    # Copy README
    if os.path.exists("README_DISTRIBUTION.md"):
        shutil.copy2("README_DISTRIBUTION.md", dist_folder)
        print("✅ Copied README_DISTRIBUTION.md")
    
    # Create zip file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"CallScheduleGenerator_{platform_name}_{timestamp}.zip"
    
    print(f"🗜️  Creating zip file: {zip_name}")
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dist_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arc_name = os.path.relpath(file_path, dist_folder)
                zipf.write(file_path, arc_name)
                print(f"  📄 Added: {arc_name}")
    
    # Clean up
    shutil.rmtree(dist_folder)
    
    print(f"\n🎉 Distribution package created successfully!")
    print(f"📦 File: {zip_name}")
    print(f"📏 Size: {os.path.getsize(zip_name) / (1024*1024):.1f} MB")
    
    print(f"\n📋 Distribution contents:")
    print(f"  • {exe_name} - Main application")
    if os.path.exists(launcher_name):
        print(f"  • {launcher_name} - Launcher script")
    print(f"  • README_DISTRIBUTION.md - Instructions")
    
    print(f"\n🚀 Ready to share!")
    print(f"Recipients can simply extract the zip and run {exe_name}")

if __name__ == "__main__":
    main() 
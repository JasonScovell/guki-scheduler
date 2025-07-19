#!/usr/bin/env python3
"""
Create simple distribution package with just the working Unix executable
"""

import os
import zipfile
import platform
from datetime import datetime
import shutil

def main():
    print("📦 Creating Simple Distribution Package")
    print("=" * 45)
    
    # Check if executable exists
    exe_path = "dist/CallScheduleGenerator/CallScheduleGenerator"
    
    if not os.path.exists(exe_path):
        print(f"❌ Executable not found: {exe_path}")
        print("Please run build_macos_app.py first!")
        return
    
    # Create distribution folder
    dist_folder = "CallScheduleGenerator_Simple"
    if os.path.exists(dist_folder):
        shutil.rmtree(dist_folder)
    
    os.makedirs(dist_folder)
    
    # Copy files
    print("📁 Creating simple distribution...")
    
    # Copy the entire CallScheduleGenerator directory
    shutil.copytree("dist/CallScheduleGenerator", f"{dist_folder}/CallScheduleGenerator")
    print("✅ Copied CallScheduleGenerator directory")
    
    # Copy launcher script
    if os.path.exists("launch_mac.sh"):
        shutil.copy2("launch_mac.sh", dist_folder)
        print("✅ Copied launch_mac.sh")
    
    # Copy README
    if os.path.exists("README_DISTRIBUTION.md"):
        shutil.copy2("README_DISTRIBUTION.md", dist_folder)
        print("✅ Copied README_DISTRIBUTION.md")
    
    # Create simple instructions
    instructions = """# Call Schedule Generator - Simple Distribution

## 🚀 Quick Start

### Option 1: Direct Run
```bash
./CallScheduleGenerator/CallScheduleGenerator
```

### Option 2: Launcher Script
```bash
./launch_mac.sh
```

### Option 3: Double-click
- Navigate to `CallScheduleGenerator` folder
- Right-click `CallScheduleGenerator` (the file)
- Select "Open"
- Click "Open" again if prompted

## 📋 What's Included
- `CallScheduleGenerator/` - Application folder with executable
- `launch_mac.sh` - Easy launcher script
- `README_DISTRIBUTION.md` - Full instructions

## ✅ Features
- Friday-only scheduling
- Personnel and group management
- Excel export
- Local database storage
- No installation required

## 🔧 Troubleshooting
If you get "permission denied":
```bash
chmod +x CallScheduleGenerator/CallScheduleGenerator
```

If you get "unidentified developer":
- Right-click → "Open" → "Open"
"""
    
    with open(f"{dist_folder}/QUICK_START.md", 'w') as f:
        f.write(instructions)
    print("✅ Created QUICK_START.md")
    
    # Create zip file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"CallScheduleGenerator_Simple_{timestamp}.zip"
    
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
    
    print(f"\n🎉 Simple distribution package created successfully!")
    print(f"📦 File: {zip_name}")
    print(f"📏 Size: {os.path.getsize(zip_name) / (1024*1024):.1f} MB")
    
    print(f"\n📋 Distribution contents:")
    print(f"  • CallScheduleGenerator/ - Application folder with executable")
    print(f"  • launch_mac.sh - Launcher script")
    print(f"  • README_DISTRIBUTION.md - Full instructions")
    print(f"  • QUICK_START.md - Simple instructions")
    
    print(f"\n🚀 Ready to share!")
    print(f"This package contains the working Unix executable in a folder structure.")

if __name__ == "__main__":
    main() 
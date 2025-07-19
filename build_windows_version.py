#!/usr/bin/env python3
"""
Instructions for building Windows version
"""

def main():
    print("🪟 Windows Version Build Instructions")
    print("=" * 50)
    print()
    print("Since you're on macOS, you'll need to build the Windows version")
    print("on a Windows machine. Here are the instructions:")
    print()
    print("📋 Steps for Windows Users:")
    print("1. Copy these files to a Windows machine:")
    print("   • call_scheduler_optimized.py")
    print("   • requirements.txt")
    print("   • build_executable.py")
    print("   • create_distribution.py")
    print("   • README_DISTRIBUTION.md")
    print()
    print("2. On Windows, open Command Prompt and run:")
    print("   python build_executable.py")
    print()
    print("3. Then create the distribution:")
    print("   python create_distribution.py")
    print()
    print("📦 Alternative: Use the macOS version")
    print("The macOS version can be shared with Mac users.")
    print("Windows users will need their own build.")
    print()
    print("🔧 Windows Requirements:")
    print("• Windows 10 or later")
    print("• Python 3.8+ installed")
    print("• pip (usually comes with Python)")
    print()
    print("📁 Files to share with Windows users:")
    files = [
        "call_scheduler_optimized.py",
        "requirements.txt", 
        "build_executable.py",
        "create_distribution.py",
        "README_DISTRIBUTION.md"
    ]
    
    for file in files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} (missing)")

if __name__ == "__main__":
    import os
    main() 
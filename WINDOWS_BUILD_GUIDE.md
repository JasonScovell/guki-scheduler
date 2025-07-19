# 🪟 Windows Executable Build Guide

## 🎯 Overview

This guide shows you how to create a Windows executable for your GUKI Scheduler app using GitHub Actions, without needing a Windows computer.

## 🚀 Quick Start (3 Steps)

### Step 1: Set Up GitHub Repository
```bash
# Run the setup script
./setup_github.sh

# Follow the instructions to create a GitHub repository
# Then push your code:
git add .
git commit -m "Initial commit - GUKI Scheduler app"
git remote add origin https://github.com/YOUR_USERNAME/guki-scheduler.git
git branch -M main
git push -u origin main
```

### Step 2: Wait for GitHub Actions Build
- GitHub will automatically detect the workflow
- Build will start on Windows servers
- Takes 5-10 minutes to complete
- Check progress in your repository's "Actions" tab

### Step 3: Download and Package
```bash
# Download the Windows executable
python download_windows_exe.py

# Create the complete package
python create_guki_scheduler_package.py
```

## 📁 What You Get

After the process completes, you'll have:
- `GUKI_Scheduler.zip` - Complete package with both Mac and Windows versions
- `GUKI_Scheduler_Windows.exe` - Standalone Windows executable
- No cloud dependency for end users

## 🔧 How It Works

### GitHub Actions Workflow
The `.github/workflows/build-windows.yml` file tells GitHub to:
1. Run on Windows servers when you push code
2. Install Python and dependencies
3. Use PyInstaller to create a standalone .exe
4. Make the .exe available for download

### Key Benefits
- ✅ **No Windows computer needed** - Builds on GitHub's Windows servers
- ✅ **Automatic** - Triggers on every code push
- ✅ **Free** - Uses GitHub's free tier
- ✅ **Professional** - Creates genuine Windows executables
- ✅ **Standalone** - No Python installation needed on Windows

## 📋 Detailed Process

### 1. Repository Setup
```bash
# Initialize git (if not already done)
git init

# Add all files (except those in .gitignore)
git add .

# Commit your code
git commit -m "Initial commit - GUKI Scheduler app"

# Add GitHub as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/guki-scheduler.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 2. Monitor Build Progress
1. Go to your GitHub repository
2. Click "Actions" tab
3. Click on "Build Windows Executable" workflow
4. Watch the build progress in real-time

### 3. Download Results
Once the build completes successfully:
1. Click on the completed workflow run
2. Scroll down to "Artifacts"
3. Click "GUKI_Scheduler_Windows" to download
4. Or use the automated script: `python download_windows_exe.py`

### 4. Create Distribution Package
```bash
# This will create the complete "GUKI Scheduler.zip"
python create_guki_scheduler_package.py
```

## 🛠️ Troubleshooting

### Build Fails
**Common causes:**
- Missing dependencies in `requirements.txt`
- Import errors in Python code
- File path issues

**Solutions:**
1. Check the "Actions" tab for error details
2. Fix the issue in your code
3. Push the fix: `git add . && git commit -m "Fix build issue" && git push`
4. GitHub will automatically rebuild

### Can't Download Executable
**If the download script fails:**
1. Manually download from GitHub Actions
2. Go to repository → Actions → Latest run → Artifacts
3. Download "GUKI_Scheduler_Windows"

### Repository Issues
**If you can't push to GitHub:**
1. Make sure repository is public (required for free Actions)
2. Check your GitHub credentials
3. Verify repository URL is correct

## 🔄 Future Updates

When you make changes to your app:
```bash
git add .
git commit -m "Updated app with new features"
git push
```

GitHub Actions will automatically:
- Build a new Windows executable
- Make it available for download
- Keep your distribution package up-to-date

## 📦 Distribution

The final `GUKI_Scheduler.zip` contains:
```
GUKI_Scheduler/
├── GUKI Scheduler Mac/
│   ├── CallScheduleGenerator/
│   └── Launch GUKI Scheduler.command
├── GUKI Scheduler Windows/
│   ├── GUKI_Scheduler_Windows.exe
│   └── Launch GUKI Scheduler.bat
└── README.md
```

## 🎯 Success Checklist

- [ ] GitHub repository created and public
- [ ] Code pushed to GitHub
- [ ] GitHub Actions workflow completed successfully
- [ ] Windows executable downloaded
- [ ] Distribution package created
- [ ] Tested on both Mac and Windows

## 📞 Support

If you encounter issues:
1. Check the GitHub Actions logs for specific errors
2. Verify all files are properly committed
3. Ensure repository is public
4. Check that `requirements.txt` includes all dependencies

---

**🎉 Congratulations!** You now have a professional Windows executable built entirely from your Mac! 
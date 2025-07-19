# GitHub Actions Setup Guide for Windows Executable

## 🚀 Quick Start

This guide will help you set up GitHub Actions to automatically build a Windows executable from your Mac.

## 📋 Prerequisites

1. **GitHub Account** (free)
2. **Git installed on your Mac**
3. **Your project code ready**

## 🔧 Step-by-Step Setup

### Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" button in the top right → "New repository"
3. Name it: `guki-scheduler`
4. Make it **Public** (required for free GitHub Actions)
5. Don't initialize with README (we'll push your existing code)
6. Click "Create repository"

### Step 2: Push Your Code to GitHub

Run these commands in your project directory:

```bash
# Initialize git repository (if not already done)
git init

# Add all your files
git add .

# Commit your files
git commit -m "Initial commit - GUKI Scheduler app"

# Add GitHub as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/guki-scheduler.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Trigger the Build

Once you push your code, GitHub Actions will automatically:
1. Detect the workflow file (`.github/workflows/build-windows.yml`)
2. Start building on a Windows server
3. Create the Windows executable
4. Make it available for download

### Step 4: Download the Windows Executable

1. Go to your GitHub repository
2. Click on "Actions" tab
3. Click on the latest workflow run
4. Scroll down to "Artifacts"
5. Click "GUKI_Scheduler_Windows" to download the .exe file

## 🔄 Future Updates

When you make changes to your code:

```bash
git add .
git commit -m "Updated app with new features"
git push
```

GitHub Actions will automatically build a new Windows executable!

## 📁 What Gets Built

The workflow will create:
- `GUKI_Scheduler_Windows.exe` - Standalone Windows executable
- All dependencies included (no Python installation needed on Windows)
- Ready to distribute to Windows users

## 🛠️ Troubleshooting

### If the build fails:
1. Check the "Actions" tab in your GitHub repository
2. Click on the failed workflow run
3. Look at the error messages
4. Common issues:
   - Missing dependencies in `requirements.txt`
   - Import errors in the Python code
   - File path issues

### If you need to rebuild manually:
1. Go to "Actions" tab
2. Click "Build Windows Executable" workflow
3. Click "Run workflow" button
4. Select "main" branch and click "Run workflow"

## 📦 Using the Built Executable

1. Download the .exe file from GitHub Actions
2. Include it in your "GUKI Scheduler" zip package
3. Windows users can run it directly (no Python needed)

## 🎯 Benefits

- ✅ No Windows computer needed
- ✅ Automatic builds on every code change
- ✅ Free (for public repositories)
- ✅ Professional-grade Windows executables
- ✅ No cloud dependency for end users

## 🔗 Next Steps

After setting this up:
1. Test the Windows executable on a Windows machine
2. Include it in your distribution package
3. Share the "GUKI Scheduler" zip with both Mac and Windows versions

---

**Need help?** The workflow file is already configured in `.github/workflows/build-windows.yml` 
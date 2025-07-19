#!/bin/bash

echo "🚀 GUKI Scheduler - GitHub Actions Setup"
echo "========================================"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first:"
    echo "   brew install git"
    echo ""
    exit 1
fi

echo "✅ Git is installed"
echo ""

# Check if this is already a git repository
if [ -d ".git" ]; then
    echo "✅ This is already a Git repository"
else
    echo "📁 Initializing Git repository..."
    git init
    echo "✅ Git repository initialized"
fi

echo ""
echo "📋 Next Steps:"
echo "=============="
echo ""
echo "1. Create a GitHub repository:"
echo "   - Go to https://github.com"
echo "   - Click '+' → 'New repository'"
echo "   - Name it: guki-scheduler"
echo "   - Make it PUBLIC (required for free GitHub Actions)"
echo "   - Don't initialize with README"
echo ""
echo "2. After creating the repository, run these commands:"
echo ""
echo "   git add ."
echo "   git commit -m 'Initial commit - GUKI Scheduler app'"
echo "   git remote add origin https://github.com/YOUR_USERNAME/guki-scheduler.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Replace 'YOUR_USERNAME' with your actual GitHub username"
echo ""
echo "4. Once you push the code, GitHub Actions will automatically:"
echo "   - Build the Windows executable"
echo "   - Make it available for download"
echo ""
echo "📖 For detailed instructions, see: setup_github_actions.md"
echo ""
echo "🎯 The workflow file is already configured in .github/workflows/build-windows.yml"
echo "" 
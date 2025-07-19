#!/usr/bin/env python3
"""
Download Windows executable from GitHub Actions
"""

import os
import requests
import zipfile
import tempfile
import shutil

def main():
    print("🪟 GUKI Scheduler - Download Windows Executable")
    print("=" * 50)
    print()
    
    print("📋 This script helps you download the Windows executable")
    print("   that was built by GitHub Actions.")
    print()
    
    # Get repository details
    repo_url = input("Enter your GitHub repository URL (e.g., https://github.com/username/guki-scheduler): ").strip()
    
    if not repo_url:
        print("❌ Repository URL is required!")
        return
    
    # Extract username and repo name
    try:
        parts = repo_url.rstrip('/').split('/')
        username = parts[-2]
        repo_name = parts[-1]
        print(f"✅ Repository: {username}/{repo_name}")
    except:
        print("❌ Invalid repository URL format!")
        return
    
    print()
    print("🔍 Searching for latest workflow run...")
    print("   (This may take a moment)")
    print()
    
    # Get latest workflow run
    api_url = f"https://api.github.com/repos/{username}/{repo_name}/actions/runs"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        runs = response.json()['workflow_runs']
        
        if not runs:
            print("❌ No workflow runs found!")
            print("   Make sure you've pushed your code to GitHub and the workflow has run.")
            return
        
        # Find the latest successful run
        latest_run = None
        for run in runs:
            if run['name'] == 'Build Windows Executable' and run['conclusion'] == 'success':
                latest_run = run
                break
        
        if not latest_run:
            print("❌ No successful Windows build found!")
            print("   Make sure the GitHub Actions workflow completed successfully.")
            return
        
        run_id = latest_run['id']
        print(f"✅ Found successful build: Run #{run_id}")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error accessing GitHub API: {e}")
        print("   Make sure the repository is public and accessible.")
        return
    
    # Get artifacts
    artifacts_url = f"https://api.github.com/repos/{username}/{repo_name}/actions/runs/{run_id}/artifacts"
    
    try:
        response = requests.get(artifacts_url)
        response.raise_for_status()
        artifacts = response.json()['artifacts']
        
        windows_artifact = None
        for artifact in artifacts:
            if artifact['name'] == 'GUKI_Scheduler_Windows':
                windows_artifact = artifact
                break
        
        if not windows_artifact:
            print("❌ Windows executable artifact not found!")
            print("   Make sure the workflow created the 'GUKI_Scheduler_Windows' artifact.")
            return
        
        artifact_id = windows_artifact['id']
        print(f"✅ Found Windows executable artifact: ID {artifact_id}")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error accessing artifacts: {e}")
        return
    
    # Download the artifact
    print()
    print("📥 Downloading Windows executable...")
    
    download_url = f"https://api.github.com/repos/{username}/{repo_name}/actions/artifacts/{artifact_id}/zip"
    
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        
        # Save to temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as temp_file:
            temp_file.write(response.content)
            temp_file_path = temp_file.name
        
        # Extract the zip
        with zipfile.ZipFile(temp_file_path, 'r') as zip_ref:
            zip_ref.extractall('.')
        
        # Clean up temp file
        os.unlink(temp_file_path)
        
        # Check if we got the executable
        if os.path.exists('GUKI_Scheduler_Windows.exe'):
            print("✅ Successfully downloaded Windows executable!")
            print(f"📁 File: GUKI_Scheduler_Windows.exe")
            print(f"📏 Size: {os.path.getsize('GUKI_Scheduler_Windows.exe') / (1024*1024):.1f} MB")
            print()
            print("🎯 Next steps:")
            print("   1. Run: python create_guki_scheduler_package.py")
            print("   2. This will create a complete package with both Mac and Windows versions")
            print("   3. Share the 'GUKI Scheduler.zip' file")
        else:
            print("❌ Windows executable not found in downloaded artifact!")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading artifact: {e}")
    except zipfile.BadZipFile:
        print("❌ Downloaded file is not a valid ZIP archive!")
    except Exception as e:
        print(f"❌ Error extracting artifact: {e}")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
GitHub Pages Setup Helper for Om Handicraft

This script helps you set up GitHub Pages with automatic syncing.
"""

import os
import json
import subprocess
import sys
from pathlib import Path

def check_git_installed():
    """Check if git is installed"""
    try:
        subprocess.run(['git', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def initialize_git_repo():
    """Initialize git repository"""
    print("🔧 Initializing Git repository...")
    
    try:
        # Initialize git if not already done
        if not Path('.git').exists():
            subprocess.run(['git', 'init'], check=True)
            print("✅ Git repository initialized")
        
        # Add all files
        subprocess.run(['git', 'add', '.'], check=True)
        print("✅ Files added to git")
        
        # Check if there are changes to commit
        result = subprocess.run(['git', 'diff', '--cached', '--quiet'], capture_output=True)
        if result.returncode != 0:
            subprocess.run(['git', 'commit', '-m', 'Initial website setup'], check=True)
            print("✅ Initial commit created")
        else:
            print("ℹ️  No changes to commit")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")
        return False

def create_github_repo_instructions():
    """Print instructions for creating GitHub repository"""
    instructions = """
🔗 GITHUB REPOSITORY SETUP

1. CREATE REPOSITORY:
   ==================
   
   a) Go to https://github.com/new
   b) Repository name: omhandicraft (or your preferred name)
   c) Description: "Handicraft business website with auto-sync"
   d) Make it PUBLIC (required for free GitHub Pages)
   e) Initialize with README
   f) Click "Create repository"

2. CONNECT LOCAL REPO:
   ===================
   
   After creating the repository, GitHub will show you commands like:
   
   git remote add origin https://github.com/YOUR_USERNAME/omhandicraft.git
   git branch -M main
   git push -u origin main
   
   Run these commands in your terminal.

3. ENABLE GITHUB PAGES:
   ====================
   
   a) Go to your repository on GitHub
   b) Click "Settings" tab
   c) Scroll to "Pages" section
   d) Source: "Deploy from a branch"
   e) Branch: "main", Folder: "/ (root)"
   f) Click "Save"
   
   Your website will be at: https://YOUR_USERNAME.github.io/omhandicraft

4. SETUP SECRETS:
   ==============
   
   a) Go to Settings → Secrets and variables → Actions
   b) Add these repository secrets:
   
   GOOGLE_SHEET_ID: your_google_sheet_id
   GOOGLE_DRIVE_FOLDER_ID: your_google_drive_folder_id
   GOOGLE_CREDENTIALS: your_google_credentials_json
   
   (Get Google credentials from Google Cloud Console)

5. TEST AUTOMATION:
   ================
   
   a) Go to "Actions" tab in your repository
   b) You should see "Sync Website Data" workflow
   c) It runs automatically every 6 hours
   d) You can also trigger it manually

🎉 YOUR WEBSITE IS NOW LIVE AND AUTO-UPDATING!
"""
    
    print(instructions)

def create_deployment_script():
    """Create a simple deployment script"""
    deploy_script = """#!/bin/bash
# Om Handicraft - GitHub Pages Deployment Script

echo "🚀 Deploying to GitHub Pages..."

# Add all changes
git add .

# Check if there are changes
if git diff --quiet --cached; then
    echo "ℹ️  No changes to commit"
else
    # Commit changes
    git commit -m "Update website content"
    
    # Push to GitHub
    git push origin main
    
    echo "✅ Website updated successfully!"
    echo "🌐 Your website will be live in a few minutes"
fi
"""
    
    with open('deploy.sh', 'w') as f:
        f.write(deploy_script)
    
    # Make it executable
    os.chmod('deploy.sh', 0o755)
    print("✅ Created deploy.sh script")

def main():
    """Main setup function"""
    print("🚀 Om Handicraft - GitHub Pages Setup")
    print("=" * 45)
    
    # Check if git is installed
    if not check_git_installed():
        print("❌ Git is not installed. Please install git first.")
        print("💡 Download from: https://git-scm.com/downloads")
        return
    
    # Initialize git repository
    if not initialize_git_repo():
        print("❌ Failed to initialize git repository")
        return
    
    # Create deployment script
    create_deployment_script()
    
    # Print instructions
    create_github_repo_instructions()
    
    print("\n✅ Local setup completed!")
    print("📁 Your files are ready to push to GitHub")
    print("🔗 Follow the instructions above to complete the setup")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Deployment Script for Om Handicraft

This script helps deploy the website and set up automation.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    try:
        import google.auth
        import googleapiclient
        print("✅ Google API libraries installed")
        return True
    except ImportError:
        print("❌ Google API libraries not installed")
        print("💡 Run: pip install -r requirements.txt")
        return False

def run_sync():
    """Run the sync script"""
    print("\n🔄 Running website sync...")
    
    try:
        result = subprocess.run([sys.executable, 'sync_website.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Website sync completed successfully")
            return True
        else:
            print(f"❌ Sync failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error running sync: {e}")
        return False

def create_deployment_package():
    """Create a deployment package"""
    print("\n📦 Creating deployment package...")
    
    deployment_files = [
        'index.html',
        'script.js',
        'data/products.json',
        'images/'
    ]
    
    deployment_dir = Path('deployment')
    deployment_dir.mkdir(exist_ok=True)
    
    for file_path in deployment_files:
        src = Path(file_path)
        dst = deployment_dir / file_path
        
        if src.is_file():
            shutil.copy2(src, dst)
            print(f"✅ Copied {file_path}")
        elif src.is_dir():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            print(f"✅ Copied {file_path}/")
        else:
            print(f"⚠️  {file_path} not found")
    
    print(f"📁 Deployment package created in {deployment_dir}/")
    return True

def print_deployment_instructions():
    """Print deployment instructions"""
    instructions = """
🚀 DEPLOYMENT INSTRUCTIONS

1. LOCAL TESTING:
   ==============
   
   a) Open index.html in your browser
   b) Test the website functionality
   c) Verify all products are displayed
   d) Test category filtering
   e) Check WhatsApp contact button

2. WEB HOSTING:
   ============
   
   Upload these files to your web hosting service:
   - index.html (main page)
   - script.js (website functionality)
   - data/products.json (product data)
   - images/ (product images)
   
   Popular hosting options:
   - GitHub Pages (free)
   - Netlify (free tier)
   - Vercel (free tier)
   - Any web hosting service

3. AUTOMATION SETUP:
   =================
   
   To automatically update the website:
   
   a) Set up a cron job (Linux/Mac):
      */30 * * * * cd /path/to/omhandicraft && python sync_website.py
   
   b) Use Task Scheduler (Windows):
      Create a task to run sync_website.py every 30 minutes
   
   c) Use GitHub Actions (if using GitHub Pages):
      Create .github/workflows/sync.yml with automation

4. GOOGLE SHEETS ACCESS:
   =====================
   
   Make sure your Google Sheet is:
   - Accessible to the script
   - Has the correct column headers
   - Contains product data
   
   Make sure your Google Drive folder:
   - Contains product images
   - Images are named correctly (product_id.jpg)
   - Folder is accessible to the script

5. TESTING:
   ========
   
   a) Add a new product to Google Sheets
   b) Upload corresponding image to Google Drive
   c) Run: python sync_website.py
   d) Check if the website updates
   e) Verify the new product appears

📞 WHATSAPP SETUP:
   ================
   
   Update the phone number in index.html:
   - Find: YOUR_PHONE_NUMBER
   - Replace with: +91XXXXXXXXXX
   - Test the WhatsApp link

🎨 CUSTOMIZATION:
   ===============
   
   - Edit index.html for colors, fonts, layout
   - Update business name and tagline
   - Modify contact information
   - Add your logo or branding

Need help? Check README.md for detailed instructions!
"""
    
    print(instructions)

def main():
    """Main deployment function"""
    print("🚀 Om Handicraft - Deployment Helper")
    print("=" * 40)
    
    # Check dependencies
    if not check_dependencies():
        print("\n💡 Please install dependencies first:")
        print("   pip install -r requirements.txt")
        return
    
    # Run sync
    if run_sync():
        print("\n✅ Website data updated successfully")
    else:
        print("\n⚠️  Website sync failed - check your configuration")
        print("💡 Run: python test_setup.py to diagnose issues")
        return
    
    # Create deployment package
    create_deployment_package()
    
    # Print instructions
    print_deployment_instructions()
    
    print("\n🎉 Deployment setup completed!")
    print("📁 Check the 'deployment/' folder for files to upload")

if __name__ == "__main__":
    main()

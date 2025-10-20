#!/usr/bin/env python3
"""
Google APIs Setup Script for Om Handicraft

This script helps you set up Google Sheets and Drive API access.
"""

import os
import json
from pathlib import Path

def create_credentials_template():
    """Create a template for Google API credentials"""
    credentials_template = {
        "installed": {
            "client_id": "YOUR_CLIENT_ID.apps.googleusercontent.com",
            "project_id": "your-project-id",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": "YOUR_CLIENT_SECRET",
            "redirect_uris": ["http://localhost"]
        }
    }
    
    with open('credentials_template.json', 'w') as f:
        json.dump(credentials_template, f, indent=2)
    
    print("✅ Created credentials_template.json")
    print("📝 Please rename this to 'credentials.json' and fill in your actual values")

def print_setup_instructions():
    """Print detailed setup instructions"""
    instructions = """
🔧 GOOGLE APIS SETUP INSTRUCTIONS

1. GOOGLE CLOUD CONSOLE SETUP:
   ============================
   
   a) Go to https://console.cloud.google.com/
   b) Create a new project or select existing one
   c) Enable the following APIs:
      - Google Sheets API
      - Google Drive API
   
   d) Go to "Credentials" → "Create Credentials" → "OAuth 2.0 Client IDs"
   e) Choose "Desktop application"
   f) Download the JSON file and rename it to 'credentials.json'
   g) Place it in this directory

2. GOOGLE SHEETS SETUP:
   ====================
   
   a) Create a new Google Sheet
   b) Add these column headers in row 1:
      - product_id
      - name  
      - category
      - size
      - price
      - availability
      - note
   
   c) Add some sample data
   d) Share the sheet with your Google account
   e) Copy the Sheet ID from the URL
      (The long string between /d/ and /edit)
   
   f) Add the Sheet ID to your .env file:
      GOOGLE_SHEET_ID=your_sheet_id_here

3. GOOGLE DRIVE SETUP:
   ===================
   
   a) Create a folder in Google Drive for product images
   b) Share the folder with your Google account
   c) Copy the folder ID from the URL
      (The long string after /folders/)
   
   d) Add the folder ID to your .env file:
      GOOGLE_DRIVE_FOLDER_ID=your_folder_id_here

4. ENVIRONMENT SETUP:
   =================
   
   a) Copy env_example.txt to .env
   b) Fill in your actual values:
      GOOGLE_SHEET_ID=your_actual_sheet_id
      GOOGLE_DRIVE_FOLDER_ID=your_actual_folder_id
      WHATSAPP_PHONE=+91XXXXXXXXXX

5. TEST THE SETUP:
   ===============
   
   a) Install dependencies: pip install -r requirements.txt
   b) Run the sync script: python sync_website.py
   c) Check if products.json is created in data/ folder
   d) Check if images are downloaded to images/ folder

📞 WHATSAPP SETUP:
   ================
   
   Update the WhatsApp phone number in index.html:
   - Find the line with "YOUR_PHONE_NUMBER"
   - Replace with your actual WhatsApp number
   - Format: +91XXXXXXXXXX (with country code)

🎨 CUSTOMIZATION:
   ===============
   
   - Edit index.html to change colors, fonts, layout
   - Update the business name and tagline
   - Modify the WhatsApp contact message
   - Add your logo or branding

🚀 DEPLOYMENT:
   ============
   
   - Upload all files to your web hosting service
   - Set up the Python script to run automatically
   - Test the complete workflow

Need help? Check the README.md for detailed instructions!
"""
    
    print(instructions)

def main():
    """Main setup function"""
    print("🚀 Om Handicraft - Google APIs Setup")
    print("=" * 50)
    
    # Create credentials template
    create_credentials_template()
    
    # Print instructions
    print_setup_instructions()
    
    print("\n✅ Setup instructions completed!")
    print("📁 Check the generated files and follow the steps above.")

if __name__ == "__main__":
    main()

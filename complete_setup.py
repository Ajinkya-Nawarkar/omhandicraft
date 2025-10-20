#!/usr/bin/env python3
"""
Complete Setup Script for Om Handicraft

This script will guide you through the entire setup process.
"""

import os
import json
import webbrowser
from pathlib import Path

def print_header():
    """Print setup header"""
    print("🚀 Om Handicraft - Complete Setup")
    print("=" * 50)
    print("I'll guide you through the entire setup process.")
    print("Let me know when you need to do something manually!\n")

def step_1_github_pages():
    """Step 1: Enable GitHub Pages"""
    print("📋 STEP 1: Enable GitHub Pages")
    print("-" * 30)
    print("I need you to do this manually:")
    print()
    print("1. Go to: https://github.com/Ajinkya-Nawarkar/omhandicraft/settings/pages")
    print("2. Under 'Source', select 'Deploy from a branch'")
    print("3. Choose 'main' branch and '/ (root)' folder")
    print("4. Click 'Save'")
    print()
    print("✅ Your website will be live at: https://ajinkya-nawarkar.github.io/omhandicraft")
    print()
    input("Press Enter when you've completed this step...")

def step_2_google_cloud():
    """Step 2: Google Cloud Console Setup"""
    print("\n📋 STEP 2: Google Cloud Console Setup")
    print("-" * 40)
    print("I need you to do this manually:")
    print()
    print("1. Go to: https://console.cloud.google.com/")
    print("2. Create a new project (or select existing)")
    print("3. Enable these APIs:")
    print("   - Google Sheets API")
    print("   - Google Drive API")
    print("4. Go to 'Credentials' → 'Create Credentials' → 'OAuth 2.0 Client IDs'")
    print("5. Choose 'Desktop application'")
    print("6. Download the JSON file")
    print("7. Save it as 'credentials.json' in this folder")
    print()
    input("Press Enter when you've completed this step...")

def step_3_google_sheets():
    """Step 3: Google Sheets Setup"""
    print("\n📋 STEP 3: Google Sheets Setup")
    print("-" * 35)
    print("I need you to do this manually:")
    print()
    print("1. Create a new Google Sheet")
    print("2. Add these column headers in row 1:")
    print("   - product_id")
    print("   - name")
    print("   - category")
    print("   - size")
    print("   - price")
    print("   - availability")
    print("   - note")
    print("3. Add some sample products")
    print("4. Copy the Sheet ID from the URL (the long string between /d/ and /edit)")
    print()
    sheet_id = input("Enter your Google Sheet ID: ").strip()
    return sheet_id

def step_4_google_drive():
    """Step 4: Google Drive Setup"""
    print("\n📋 STEP 4: Google Drive Setup")
    print("-" * 35)
    print("I need you to do this manually:")
    print()
    print("1. Create a folder in Google Drive for product images")
    print("2. Upload some sample images")
    print("3. Name images exactly like your product IDs (e.g., pottery-001.jpg)")
    print("4. Copy the folder ID from the URL (the long string after /folders/)")
    print()
    folder_id = input("Enter your Google Drive folder ID: ").strip()
    return folder_id

def step_5_configure_website():
    """Step 5: Configure Website"""
    print("\n📋 STEP 5: Configure Website")
    print("-" * 30)
    print("I'll update your website configuration...")
    
    # Get business details
    business_name = input("Business name [Om Handicraft]: ").strip() or "Om Handicraft"
    tagline = input("Tagline [Handmade Gift Items & Crafts]: ").strip() or "Handmade Gift Items & Crafts"
    whatsapp = input("WhatsApp phone (+91XXXXXXXXXX): ").strip()
    
    return {
        "business_name": business_name,
        "tagline": tagline,
        "whatsapp": whatsapp
    }

def update_config(sheet_id, folder_id, business_info):
    """Update configuration file"""
    print("\n🔧 Updating configuration...")
    
    config = {
        "business": {
            "name": business_info["business_name"],
            "tagline": business_info["tagline"],
            "whatsapp_phone": business_info["whatsapp"],
            "whatsapp_message": "Hi! I'm interested in your handicraft products. Can you tell me more about availability and pricing?"
        },
        "website": {
            "theme": {
                "primary_color": "#f59e0b",
                "secondary_color": "#ea580c",
                "accent_color": "#dc2626"
            },
            "features": {
                "show_availability": True,
                "show_sizes": True,
                "show_notes": True,
                "enable_category_filter": True
            }
        },
        "google": {
            "sheet_id": sheet_id,
            "drive_folder_id": folder_id
        }
    }
    
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("✅ Configuration updated!")

def step_6_github_secrets():
    """Step 6: GitHub Secrets"""
    print("\n📋 STEP 6: GitHub Secrets")
    print("-" * 25)
    print("I need you to do this manually:")
    print()
    print("1. Go to: https://github.com/Ajinkya-Nawarkar/omhandicraft/settings/secrets/actions")
    print("2. Click 'New repository secret' and add these:")
    print()
    print("Secret 1:")
    print("Name: GOOGLE_SHEET_ID")
    print(f"Value: {sheet_id}")
    print()
    print("Secret 2:")
    print("Name: GOOGLE_DRIVE_FOLDER_ID")
    print(f"Value: {folder_id}")
    print()
    print("Secret 3:")
    print("Name: GOOGLE_CREDENTIALS")
    print("Value: [Copy the entire contents of your credentials.json file]")
    print()
    input("Press Enter when you've added all three secrets...")

def step_7_test_automation():
    """Step 7: Test Automation"""
    print("\n📋 STEP 7: Test Automation")
    print("-" * 30)
    print("Let's test if everything works:")
    print()
    print("1. Go to: https://github.com/Ajinkya-Nawarkar/omhandicraft/actions")
    print("2. Click 'Sync Website Data' workflow")
    print("3. Click 'Run workflow' button")
    print("4. Check if it runs successfully")
    print()
    print("✅ If successful, your website will update automatically every 6 hours!")
    print()
    input("Press Enter when you've tested the workflow...")

def step_8_final_check():
    """Step 8: Final Check"""
    print("\n🎉 FINAL CHECK")
    print("-" * 20)
    print("Your website should now be live at:")
    print("https://ajinkya-nawarkar.github.io/omhandicraft")
    print()
    print("✅ Check if the website loads")
    print("✅ Check if products are displayed")
    print("✅ Check if WhatsApp contact works")
    print("✅ Check if category filtering works")
    print()
    print("🎯 Your website is now fully automated!")
    print("Just update your Google Sheet and images to update the website.")

def main():
    """Main setup function"""
    print_header()
    
    # Step 1: GitHub Pages
    step_1_github_pages()
    
    # Step 2: Google Cloud Console
    step_2_google_cloud()
    
    # Step 3: Google Sheets
    sheet_id = step_3_google_sheets()
    
    # Step 4: Google Drive
    folder_id = step_4_google_drive()
    
    # Step 5: Configure Website
    business_info = step_5_configure_website()
    
    # Update configuration
    update_config(sheet_id, folder_id, business_info)
    
    # Step 6: GitHub Secrets
    step_6_github_secrets()
    
    # Step 7: Test Automation
    step_7_test_automation()
    
    # Step 8: Final Check
    step_8_final_check()
    
    print("\n🎉 Setup Complete!")
    print("Your handicraft website is now live and fully automated!")

if __name__ == "__main__":
    main()

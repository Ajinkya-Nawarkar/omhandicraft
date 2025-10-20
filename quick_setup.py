#!/usr/bin/env python3
"""
Quick Setup Script for Om Handicraft
"""

import json
import os

def main():
    print("🚀 Om Handicraft - Quick Setup")
    print("=" * 40)
    
    print("\n📋 Let's configure your website:")
    
    # Get business details
    business_name = input("Business name [Om Handicraft]: ").strip() or "Om Handicraft"
    tagline = input("Tagline [Handmade Gift Items & Crafts]: ").strip() or "Handmade Gift Items & Crafts"
    whatsapp = input("WhatsApp phone (+91XXXXXXXXXX): ").strip()
    
    print(f"\n✅ Business: {business_name}")
    print(f"✅ Tagline: {tagline}")
    print(f"✅ WhatsApp: {whatsapp}")
    
    # Update config
    config = {
        "business": {
            "name": business_name,
            "tagline": tagline,
            "whatsapp_phone": whatsapp,
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
            "sheet_id": "YOUR_GOOGLE_SHEET_ID",
            "drive_folder_id": "YOUR_GOOGLE_DRIVE_FOLDER_ID"
        }
    }
    
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("\n✅ Configuration updated!")
    print("\n📋 Next steps:")
    print("1. Create your Google Sheet and get the Sheet ID")
    print("2. Create your Google Drive folder and get the folder ID")
    print("3. Update config.json with those IDs")
    print("4. Enable GitHub Pages")
    print("5. Add GitHub secrets")
    print("6. Test the automation")
    
    print(f"\n🌐 Your website will be at: https://ajinkya-nawarkar.github.io/omhandicraft")

if __name__ == "__main__":
    main()

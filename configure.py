#!/usr/bin/env python3
"""
Configuration Helper for Om Handicraft

This script helps you configure the website easily.
"""

import json
import os
from pathlib import Path

def load_config():
    """Load existing configuration"""
    config_path = Path('config.json')
    if config_path.exists():
        with open(config_path, 'r') as f:
            return json.load(f)
    return {}

def save_config(config):
    """Save configuration to file"""
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=2)

def configure_business():
    """Configure business information"""
    print("\n🏢 Business Configuration")
    print("=" * 30)
    
    name = input("Business Name [Om Handicraft]: ").strip() or "Om Handicraft"
    tagline = input("Tagline [Handmade Gift Items & Crafts]: ").strip() or "Handmade Gift Items & Crafts"
    phone = input("WhatsApp Phone (+91XXXXXXXXXX): ").strip()
    message = input("Default WhatsApp Message [Hi! I'm interested in your handicraft products. Can you tell me more about availability and pricing?]: ").strip() or "Hi! I'm interested in your handicraft products. Can you tell me more about availability and pricing?"
    
    return {
        "name": name,
        "tagline": tagline,
        "whatsapp_phone": phone,
        "whatsapp_message": message
    }

def configure_google():
    """Configure Google services"""
    print("\n🔗 Google Services Configuration")
    print("=" * 35)
    
    sheet_id = input("Google Sheet ID: ").strip()
    drive_folder_id = input("Google Drive Folder ID: ").strip()
    
    return {
        "sheet_id": sheet_id,
        "drive_folder_id": drive_folder_id
    }

def configure_theme():
    """Configure website theme"""
    print("\n🎨 Website Theme Configuration")
    print("=" * 32)
    
    print("Choose a color scheme:")
    print("1. Amber/Orange (Default)")
    print("2. Blue/Teal")
    print("3. Green/Emerald")
    print("4. Purple/Violet")
    print("5. Custom")
    
    choice = input("Enter choice (1-5) [1]: ").strip() or "1"
    
    themes = {
        "1": {"primary": "#f59e0b", "secondary": "#ea580c", "accent": "#dc2626"},
        "2": {"primary": "#0ea5e9", "secondary": "#0891b2", "accent": "#0284c7"},
        "3": {"primary": "#10b981", "secondary": "#059669", "accent": "#047857"},
        "4": {"primary": "#8b5cf6", "secondary": "#7c3aed", "accent": "#6d28d9"},
        "5": {
            "primary": input("Primary color (hex): ").strip() or "#f59e0b",
            "secondary": input("Secondary color (hex): ").strip() or "#ea580c",
            "accent": input("Accent color (hex): ").strip() or "#dc2626"
        }
    }
    
    return themes.get(choice, themes["1"])

def configure_features():
    """Configure website features"""
    print("\n⚙️ Website Features")
    print("=" * 20)
    
    show_availability = input("Show availability status? (y/n) [y]: ").strip().lower() != 'n'
    show_sizes = input("Show product sizes? (y/n) [y]: ").strip().lower() != 'n'
    show_notes = input("Show product notes? (y/n) [y]: ").strip().lower() != 'n'
    enable_category_filter = input("Enable category filtering? (y/n) [y]: ").strip().lower() != 'n'
    
    return {
        "show_availability": show_availability,
        "show_sizes": show_sizes,
        "show_notes": show_notes,
        "enable_category_filter": enable_category_filter
    }

def main():
    """Main configuration function"""
    print("🔧 Om Handicraft - Configuration Helper")
    print("=" * 45)
    
    # Load existing config
    config = load_config()
    
    # Configure each section
    business_config = configure_business()
    google_config = configure_google()
    theme_config = configure_theme()
    features_config = configure_features()
    
    # Build final configuration
    final_config = {
        "business": business_config,
        "website": {
            "theme": theme_config,
            "features": features_config
        },
        "google": google_config
    }
    
    # Save configuration
    save_config(final_config)
    
    print("\n✅ Configuration saved to config.json")
    print("\n📋 Next steps:")
    print("1. Set up Google API credentials (credentials.json)")
    print("2. Test the setup: python test_setup.py")
    print("3. Sync your data: python sync_website.py")
    print("4. Deploy the website: python deploy.py")

if __name__ == "__main__":
    main()

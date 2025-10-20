#!/usr/bin/env python3
"""
Test Setup Script for Om Handicraft

This script tests if everything is configured correctly.
"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv

def test_environment():
    """Test environment configuration"""
    print("🔍 Testing Environment Configuration...")
    
    load_dotenv()
    
    required_vars = ['GOOGLE_SHEET_ID', 'GOOGLE_DRIVE_FOLDER_ID']
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"❌ Missing environment variables: {', '.join(missing_vars)}")
        print("💡 Please update your .env file with the correct values")
        return False
    else:
        print("✅ Environment variables configured")
        return True

def test_files():
    """Test if required files exist"""
    print("\n🔍 Testing Required Files...")
    
    required_files = [
        'index.html',
        'script.js',
        'sync_website.py',
        'requirements.txt'
    ]
    
    missing_files = []
    
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    else:
        print("✅ All required files present")
        return True

def test_directories():
    """Test if required directories exist"""
    print("\n🔍 Testing Directory Structure...")
    
    required_dirs = ['data', 'images']
    
    for dir_name in required_dirs:
        dir_path = Path(dir_name)
        if not dir_path.exists():
            dir_path.mkdir(exist_ok=True)
            print(f"✅ Created directory: {dir_name}")
        else:
            print(f"✅ Directory exists: {dir_name}")

def test_credentials():
    """Test Google API credentials"""
    print("\n🔍 Testing Google API Credentials...")
    
    if not Path('credentials.json').exists():
        print("❌ credentials.json not found")
        print("💡 Please download your OAuth credentials from Google Cloud Console")
        return False
    else:
        print("✅ credentials.json found")
        return True

def test_website_files():
    """Test if website files are properly structured"""
    print("\n🔍 Testing Website Structure...")
    
    # Test HTML file
    if Path('index.html').exists():
        with open('index.html', 'r') as f:
            content = f.read()
            if 'Om Handicraft' in content:
                print("✅ HTML file contains correct business name")
            else:
                print("⚠️  HTML file may need customization")
    
    # Test JavaScript file
    if Path('script.js').exists():
        with open('script.js', 'r') as f:
            content = f.read()
            if 'OmHandicraft' in content:
                print("✅ JavaScript file properly configured")
            else:
                print("⚠️  JavaScript file may need review")

def test_sample_data():
    """Test sample data structure"""
    print("\n🔍 Testing Sample Data...")
    
    data_file = Path('data/products.json')
    if data_file.exists():
        try:
            with open(data_file, 'r') as f:
                data = json.load(f)
                if 'products' in data and 'categories' in data:
                    print(f"✅ Sample data loaded: {len(data['products'])} products, {len(data['categories'])} categories")
                    return True
                else:
                    print("❌ Sample data structure incorrect")
                    return False
        except json.JSONDecodeError:
            print("❌ Sample data file corrupted")
            return False
    else:
        print("⚠️  No sample data found - this is normal for first setup")
        return True

def main():
    """Main test function"""
    print("🧪 Om Handicraft - Setup Test")
    print("=" * 40)
    
    tests = [
        test_environment,
        test_files,
        test_directories,
        test_credentials,
        test_website_files,
        test_sample_data
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your setup is ready.")
        print("🚀 You can now run: python sync_website.py")
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
        print("💡 Run: python setup_google_apis.py for setup instructions")

if __name__ == "__main__":
    main()

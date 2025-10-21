#!/usr/bin/env python3
"""
Om Handicraft Website Sync Script

This script syncs product data from Google Sheets and images from Google Drive
to update the website automatically.

Usage:
    python sync_website.py

Requirements:
    - Google Sheets API credentials
    - Google Drive API credentials
    - .env file with configuration
"""

import os
import json
import logging
from typing import List, Dict, Any
from pathlib import Path
from dotenv import load_dotenv

# Google API imports
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class OmHandicraftSync:
    def __init__(self):
        self.sheets_service = None
        self.drive_service = None
        self.website_path = Path(__file__).parent
        self.images_path = self.website_path / 'images'
        self.data_path = self.website_path / 'data'
        
        # Load configuration
        self.config = self.load_config()
        self.spreadsheet_id = self.config.get('google', {}).get('sheet_id')
        self.drive_folder_id = self.config.get('google', {}).get('drive_folder_id')
        
        # Create directories if they don't exist
        self.images_path.mkdir(exist_ok=True)
        self.data_path.mkdir(exist_ok=True)

    def load_config(self):
        """Load configuration from config.json"""
        try:
            config_path = self.website_path / 'config.json'
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Could not load config.json: {e}")
            # Fallback to environment variables
            return {
                'google': {
                    'sheet_id': os.getenv('GOOGLE_SHEET_ID'),
                    'drive_folder_id': os.getenv('GOOGLE_DRIVE_FOLDER_ID')
                }
            }

    def authenticate_google_apis(self):
        """Authenticate with Google APIs"""
        try:
            SCOPES = [
                'https://www.googleapis.com/auth/spreadsheets.readonly',
                'https://www.googleapis.com/auth/drive.readonly'
            ]
            
            if os.getenv('GITHUB_ACTIONS'):
                # GitHub Actions - use Service Account credentials from secrets
                logger.info("Running in GitHub Actions - using service account credentials")
                
                # Get credentials from GitHub Secrets
                credentials_json = os.getenv('GOOGLE_CREDENTIALS')
                if not credentials_json:
                    raise ValueError("GOOGLE_CREDENTIALS environment variable not set")
                
                # Parse the service account credentials JSON
                import json
                credentials_info = json.loads(credentials_json)
                
                # Create service account credentials
                from google.oauth2 import service_account
                creds = service_account.Credentials.from_service_account_info(
                    credentials_info, scopes=SCOPES)
                
            else:
                # Local development - use OAuth flow
                creds = None
                token_file = 'token.json'
                
                if os.path.exists(token_file):
                    creds = Credentials.from_authorized_user_file(token_file, SCOPES)
                
                if not creds or not creds.valid:
                    if creds and creds.expired and creds.refresh_token:
                        creds.refresh(Request())
                    else:
                        flow = InstalledAppFlow.from_client_secrets_file(
                            'credentials.json', SCOPES)
                        creds = flow.run_local_server(port=0)
                    
                    with open(token_file, 'w') as token:
                        token.write(creds.to_json())
            
            # Build services
            self.sheets_service = build('sheets', 'v4', credentials=creds)
            self.drive_service = build('drive', 'v3', credentials=creds)
            
            logger.info("Successfully authenticated with Google APIs")
            return True
            
        except Exception as e:
            logger.error(f"Authentication failed: {e}")
            return False

    def get_products_from_sheets(self) -> List[Dict[str, Any]]:
        """Fetch products from Google Sheets"""
        try:
            if not self.sheets_service:
                raise ValueError("Sheets service not initialized")
            
            if not self.spreadsheet_id:
                raise ValueError("Google Sheet ID not configured")
            
            range_name = 'Sheet1!A:G'  # Adjust range as needed
            result = self.sheets_service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=range_name
            ).execute()
            
            values = result.get('values', [])
            if not values:
                logger.warning("No data found in Google Sheets")
                return []
            
            # Skip header row
            headers = values[0]
            products = []
            
            for row in values[1:]:
                if len(row) >= 7:  # Ensure we have all required columns
                    product = {
                        'id': row[0],
                        'name': row[1],
                        'category': row[2],
                        'size': row[3],
                        'price': int(row[4]) if row[4].isdigit() else 0,
                        'availability': row[5],
                        'image': f"{row[0]}.jpg",  # Default to jpg
                        'note': row[6] if len(row) > 6 else ''
                    }
                    products.append(product)
            
            logger.info(f"Fetched {len(products)} products from Google Sheets")
            return products
            
        except HttpError as e:
            logger.error(f"Error fetching from Google Sheets: {e}")
            return []

    def get_sample_products(self) -> List[Dict[str, Any]]:
        """Get sample products for testing"""
        return [
            {
                'id': 'pottery-001',
                'name': 'Handmade Ceramic Bowl',
                'category': 'Pottery',
                'size': 'Medium',
                'price': 450,
                'availability': 'In Stock',
                'image': 'pottery-001.jpg',
                'note': 'Beautiful handcrafted ceramic bowl perfect for serving'
            },
            {
                'id': 'pottery-002',
                'name': 'Handmade Ceramic Bowl',
                'category': 'Pottery',
                'size': 'Large',
                'price': 650,
                'availability': 'In Stock',
                'image': 'pottery-002.jpg',
                'note': 'Beautiful handcrafted ceramic bowl perfect for serving'
            },
            {
                'id': 'wood-001',
                'name': 'Carved Wooden Box',
                'category': 'Woodwork',
                'size': 'Small',
                'price': 800,
                'availability': 'Limited Stock',
                'image': 'wood-001.jpg',
                'note': 'Hand-carved wooden jewelry box with intricate details'
            }
        ]

    def get_categories_from_products(self, products: List[Dict[str, Any]]) -> List[str]:
        """Extract unique categories from products"""
        categories = list(set(product['category'] for product in products))
        return sorted(categories)

    def download_image_from_drive(self, product_id: str) -> bool:
        """Download product image from Google Drive"""
        try:
            if not self.drive_service:
                raise ValueError("Drive service not initialized")
            
            if not self.drive_folder_id:
                raise ValueError("Google Drive folder ID not configured")
            
            # Search for file in Google Drive
            query = f"name='{product_id}' and parents in '{self.drive_folder_id}'"
            results = self.drive_service.files().list(
                q=query,
                fields="files(id, name, mimeType)"
            ).execute()
            
            files = results.get('files', [])
            if not files:
                logger.warning(f"Image not found for product {product_id}")
                return False
            
            # Get the first matching file
            file_info = files[0]
            file_id = file_info['id']
            
            # Download the file
            request = self.drive_service.files().get_media(fileId=file_id)
            file_path = self.images_path / f"{product_id}.jpg"
            
            with open(file_path, 'wb') as f:
                f.write(request.execute())
            
            logger.info(f"Downloaded image for product {product_id}")
            return True
            
        except Exception as e:
            logger.error(f"Error downloading image for {product_id}: {e}")
            return False

    def update_products_json(self, products: List[Dict[str, Any]], categories: List[str]):
        """Update the products.json file"""
        try:
            data = {
                'products': products,
                'categories': categories,
                'last_updated': str(Path().cwd())  # Simple timestamp placeholder
            }
            
            json_path = self.data_path / 'products.json'
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Updated products.json with {len(products)} products and {len(categories)} categories")
            
        except Exception as e:
            logger.error(f"Error updating products.json: {e}")

    def sync_website(self):
        """Main sync function"""
        logger.info("Starting website sync...")
        
        # Authenticate
        if not self.authenticate_google_apis():
            logger.error("Authentication failed. Please check your credentials.")
            return False
        
        # Get products from Google Sheets
        products = self.get_products_from_sheets()
        if not products:
            logger.warning("No products found. Website will show empty state.")
            return False
        
        # Get categories
        categories = self.get_categories_from_products(products)
        
        # Download images
        for product in products:
            self.download_image_from_drive(product['id'])
        
        # Update products.json
        self.update_products_json(products, categories)
        
        logger.info("Website sync completed successfully!")
        return True

def main():
    """Main function"""
    sync = OmHandicraftSync()
    success = sync.sync_website()
    
    if success:
        print("✅ Website sync completed successfully!")
        print("🌐 Your website has been updated with the latest products.")
    else:
        print("❌ Website sync failed. Please check the logs for details.")
        print("💡 Make sure your Google Sheets and Drive are properly configured.")

if __name__ == "__main__":
    main()

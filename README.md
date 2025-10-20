# Om Handicraft Website

A simple, maintainable website for a handicraft business that allows non-tech-savvy users to update products via Google Sheets.

## Features

- 🎨 **Modern Design**: Clean, responsive UI with glassmorphism effects
- 📱 **Mobile Friendly**: Works perfectly on all devices
- 🔄 **Easy Updates**: Update products via Google Sheets
- 📸 **Image Management**: Automatic image sync from Google Drive
- 💬 **WhatsApp Integration**: Direct contact for orders
- 🏷️ **Category Filtering**: Organize products by categories
- ⚡ **Fast Loading**: Static site with optimized performance

## Quick Start

### Option 1: GitHub Pages (Recommended)

**Automatic updates, free hosting, custom domain support**

```bash
# Setup GitHub Pages
python setup_github.py

# Follow the instructions to:
# 1. Create GitHub repository
# 2. Enable GitHub Pages
# 3. Configure secrets
# 4. Your website auto-updates every 6 hours!
```

### Option 2: Manual Hosting

**Upload files to any web hosting service**

1. **Setup Google Sheets & Drive** (same for both options)
2. **Configure the website** (same for both options)
3. **Upload files manually** to your hosting service

### 1. Setup Google Sheets

1. Create a Google Sheet with these columns:
   - `product_id` (e.g., pottery-001)
   - `name` (e.g., Handmade Ceramic Bowl)
   - `category` (e.g., Pottery)
   - `size` (e.g., Medium)
   - `price` (e.g., 450)
   - `availability` (e.g., In Stock)
   - `note` (e.g., Beautiful handcrafted bowl)

2. Add your products to the sheet

### 2. Setup Google Drive

1. Create a folder in Google Drive for product images
2. Upload images with filenames matching product IDs (e.g., pottery-001.jpg)

### 3. Configure the Website

1. Edit `config.json` with your settings:
   - Update `business.name` and `business.tagline`
   - Set your `whatsapp_phone` number
   - Add your `google.sheet_id` and `google.drive_folder_id`
   - Customize colors and features as needed

### 4. Setup Python Environment

```bash
# Install dependencies
pip install -r requirements.txt

# Setup Google API credentials
# Download credentials.json from Google Cloud Console
# Run the sync script
python sync_website.py
```

### 5. Deploy the Website

**GitHub Pages (Recommended):**
- Automatic updates daily at midnight
- Free hosting
- Custom domain support
- No server management needed

**Manual Hosting:**
- Upload files to any web hosting service
- Manual updates required

## File Structure

```
omhandicraft/
├── index.html              # Main website file
├── script.js               # Website JavaScript
├── sync_website.py         # Python sync script
├── requirements.txt        # Python dependencies
├── data/
│   └── products.json       # Generated product data
├── images/                 # Product images
└── README.md              # This file
```

## How It Works

1. **Google Sheets**: Store all product information
2. **Google Drive**: Store product images
3. **Python Script**: Syncs data from Sheets/Drive to website
4. **Static Website**: Displays products with modern UI
5. **WhatsApp**: Customers can contact directly for orders

## For Non-Tech Users

### Adding New Products
1. Open your Google Sheet
2. Add a new row with product details
3. Upload image to Google Drive with matching filename
4. Run the sync script (or set up automation)

### Updating Products
1. Edit the row in Google Sheet
2. Replace image in Google Drive if needed
3. Run the sync script

### Removing Products
1. Delete the row from Google Sheet
2. Run the sync script

## Customization

### Styling
- Edit `index.html` to change colors, fonts, layout
- The design uses Tailwind CSS for easy customization

### WhatsApp Contact
- Update the phone number in `index.html`
- Change the contact message as needed

### Categories
- Add new categories in Google Sheets
- The website will automatically update

## Automation

Set up the Python script to run automatically:
- **Cron Job** (Linux/Mac): Run every hour/day
- **Task Scheduler** (Windows): Set up recurring task
- **GitHub Actions**: For automated deployment

## Support

For technical issues:
1. Check the logs in the Python script
2. Verify Google API credentials
3. Ensure Google Sheets/Drive permissions

## License

This project is open source and available under the MIT License.

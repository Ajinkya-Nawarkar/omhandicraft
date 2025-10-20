# GitHub Pages Setup Guide

## 🚀 Complete GitHub Pages Setup

### Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and create a new repository
2. Name it: `omhandicraft` (or your preferred name)
3. Make it **Public** (required for free GitHub Pages)
4. Initialize with README

### Step 2: Upload Your Files

```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/omhandicraft.git
cd omhandicraft

# Copy all your website files here
# (index.html, script.js, config.json, etc.)

# Add and commit files
git add .
git commit -m "Initial website setup"
git push origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll down to **Pages** section
4. Under **Source**, select **Deploy from a branch**
5. Choose **main** branch and **/ (root)** folder
6. Click **Save**

Your website will be available at:
`https://YOUR_USERNAME.github.io/omhandicraft`

### Step 4: Setup Custom Domain (Optional)

1. In GitHub Pages settings, add your custom domain
2. Update your domain's DNS settings:
   - Add CNAME record pointing to `YOUR_USERNAME.github.io`
3. Your website will be available at your custom domain

### Step 5: Configure GitHub Secrets

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Add these repository secrets:

#### Required Secrets:
- `GOOGLE_SHEET_ID`: Your Google Sheet ID
- `GOOGLE_DRIVE_FOLDER_ID`: Your Google Drive folder ID  
- `GOOGLE_CREDENTIALS`: Your Google API credentials JSON

#### How to get Google Credentials:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google Sheets API and Google Drive API
4. Create OAuth 2.0 credentials
5. Download the JSON file
6. Copy the entire JSON content to `GOOGLE_CREDENTIALS` secret

### Step 6: Test the Setup

1. Go to **Actions** tab in your repository
2. You should see the "Sync Website Data" workflow
3. It will run automatically daily at midnight
4. You can also trigger it manually

## 🔄 How It Works

### Automatic Updates:
1. **Daily at midnight**: GitHub Actions runs the sync script
2. **Script reads**: Google Sheets and Google Drive
3. **Updates**: `data/products.json` and `images/` folder
4. **Commits**: Changes back to the repository
5. **GitHub Pages**: Automatically rebuilds the website

### Manual Updates:
1. **Update Google Sheet**: Add/edit products
2. **Upload images**: To Google Drive folder
3. **Trigger sync**: Go to Actions → "Sync Website Data" → "Run workflow"

## 📁 Repository Structure

```
omhandicraft/
├── .github/
│   └── workflows/
│       └── sync-website.yml    # Auto-sync workflow
├── .gitignore                  # Ignore sensitive files
├── index.html                  # Main website
├── script.js                   # Website functionality
├── config.json                 # Configuration
├── data/
│   └── products.json           # Generated product data
├── images/                     # Product images
├── requirements.txt            # Python dependencies
├── sync_website.py            # Sync script
└── README.md                  # Documentation
```

## 🎯 Benefits of This Setup

✅ **Fully Automated**: Updates every 6 hours automatically  
✅ **Free Hosting**: GitHub Pages is completely free  
✅ **Custom Domain**: Use your own domain name  
✅ **Version Control**: All changes are tracked  
✅ **Easy Maintenance**: Just update Google Sheets  
✅ **No Server Management**: GitHub handles everything  

## 🔧 For Non-Tech Users

### To Add New Products:
1. Open your Google Sheet
2. Add new product row
3. Upload image to Google Drive
4. Wait until midnight (or trigger manually)

### To Update Products:
1. Edit the row in Google Sheet
2. Replace image in Google Drive if needed
3. Changes appear automatically

### To Change Website Settings:
1. Edit `config.json` in the repository
2. Commit and push changes
3. Website updates immediately

## 🚨 Important Notes

- **Keep credentials secure**: Never commit `credentials.json` to the repository
- **Public repository**: Required for free GitHub Pages
- **Google API limits**: Be aware of API quotas
- **Image optimization**: Large images may slow down the site

## 🆘 Troubleshooting

### Website not updating?
- Check GitHub Actions logs
- Verify Google API credentials
- Check Google Sheets permissions

### Images not loading?
- Verify image filenames match product IDs
- Check Google Drive folder permissions
- Ensure images are in the correct folder

### Sync not working?
- Check repository secrets are set correctly
- Verify Google API credentials
- Check Google Sheets/Drive access

Need help? Check the GitHub Actions logs for detailed error messages!

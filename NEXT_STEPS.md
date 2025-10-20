# 🚀 Next Steps - GitHub Pages Setup

## ✅ Repository Setup Complete!

Your repository is now live at: https://github.com/Ajinkya-Nawarkar/omhandicraft.git

## 🔧 Next Steps to Get Your Website Live:

### 1. Enable GitHub Pages
1. Go to your repository: https://github.com/Ajinkya-Nawarkar/omhandicraft
2. Click **Settings** tab
3. Scroll down to **Pages** section (left sidebar)
4. Under **Source**, select **Deploy from a branch**
5. Choose **main** branch and **/ (root)** folder
6. Click **Save**

Your website will be live at: **https://ajinkya-nawarkar.github.io/omhandicraft**

### 2. Configure Google API Secrets
1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret** and add these:

#### Required Secrets:
- **Name**: `GOOGLE_SHEET_ID`
  **Value**: Your Google Sheet ID (get from Google Sheets URL)

- **Name**: `GOOGLE_DRIVE_FOLDER_ID` 
  **Value**: Your Google Drive folder ID (get from folder URL)

- **Name**: `GOOGLE_CREDENTIALS`
  **Value**: Your Google API credentials JSON (get from Google Cloud Console)

### 3. Get Google API Credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable these APIs:
   - Google Sheets API
   - Google Drive API
4. Go to **Credentials** → **Create Credentials** → **OAuth 2.0 Client IDs**
5. Choose **Desktop application**
6. Download the JSON file
7. Copy the entire JSON content to the `GOOGLE_CREDENTIALS` secret

### 4. Test the Automation
1. Go to **Actions** tab in your repository
2. You should see **"Sync Website Data"** workflow
3. Click on it and **"Run workflow"** to test
4. Check if it runs successfully

### 5. Update Your Configuration
Edit `config.json` in your repository with your business details:
- Business name and tagline
- WhatsApp phone number
- Google Sheet and Drive IDs

## 🎯 What Happens Next:

- **Every 6 hours**: GitHub automatically syncs your Google Sheets data
- **Updates**: Your website updates automatically with new products
- **Images**: Automatically downloads from Google Drive
- **Zero maintenance**: Just update Google Sheets and images

## 🌐 Your Website URLs:

- **GitHub Pages**: https://ajinkya-nawarkar.github.io/omhandicraft
- **Custom Domain**: You can add your own domain later

## 🔄 For Ongoing Updates:

### To Add New Products:
1. Update your Google Sheet
2. Upload image to Google Drive
3. Wait up to 6 hours (or trigger manually in Actions)

### To Update Website Settings:
1. Edit `config.json` in GitHub
2. Commit changes
3. Website updates immediately

## 🆘 Need Help?

- Check the **Actions** tab for workflow logs
- Verify your Google API credentials
- Check Google Sheets/Drive permissions

Your website is almost ready! 🎉

# Private Configuration Setup

## 🔒 **Privacy Protection**

To keep your personal information private, follow these steps:

### **Step 1: Create Private Config File**
1. **Copy** `config.json` to `config.private.json`
2. **Update** `config.private.json` with your real information:
   ```json
   {
     "business": {
       "whatsapp_phone": "+919881477561",
       "whatsapp_message": "Your custom message here"
     },
     "google": {
       "sheet_id": "your_real_google_sheet_id",
       "drive_folder_id": "your_real_google_drive_folder_id"
     }
   }
   ```

### **Step 2: Update Website to Use Private Config**
The website will automatically use `config.private.json` if it exists, otherwise fall back to `config.json`.

### **Step 3: Never Commit Private Files**
- ✅ **config.private.json** - Added to .gitignore
- ✅ **credentials.json** - Already in .gitignore
- ✅ **token.json** - Already in .gitignore

## 🚀 **For Production:**

### **GitHub Actions:**
- Use **GitHub Secrets** for sensitive data
- **GOOGLE_CREDENTIALS** - Service account JSON
- **GOOGLE_SHEET_ID** - Your sheet ID
- **GOOGLE_DRIVE_FOLDER_ID** - Your folder ID

### **Local Development:**
- Use **config.private.json** for real data
- Keep **config.json** with placeholder data

## ✅ **Privacy Checklist:**
- ✅ **Phone number** - Not in public repository
- ✅ **Google credentials** - Not in public repository
- ✅ **API keys** - Not in public repository
- ✅ **Personal data** - Protected by .gitignore

## 🔧 **Quick Setup:**
1. **Copy config.json to config.private.json**
2. **Update with your real data**
3. **Test locally** - Should work with real phone number
4. **Deploy** - GitHub Actions will use secrets

**Your personal information is now protected!** 🔒✨

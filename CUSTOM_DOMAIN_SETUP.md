# Custom Domain Setup for omhandicraft.com

## GitHub Pages Configuration

### 1. Repository Settings
- Go to your repository: https://github.com/Ajinkya-Nawarkar/omhandicraft
- Click **Settings** → **Pages**
- Under **Custom domain**, enter: `omhandicraft.com`
- Check **Enforce HTTPS** (recommended)

### 2. DNS Configuration
You need to configure your domain's DNS records with your domain provider:

#### Option A: Apex Domain (omhandicraft.com)
Add these A records:
```
Type: A
Name: @
Value: 185.199.108.153
Value: 185.199.109.153
Value: 185.199.110.153
Value: 185.199.111.153
```

#### Option B: WWW Subdomain (www.omhandicraft.com)
Add this CNAME record:
```
Type: CNAME
Name: www
Value: ajinkya-nawarkar.github.io
```

### 3. Verification
After DNS propagation (can take up to 24 hours):
- Visit: https://omhandicraft.com
- Should redirect to your GitHub Pages site
- Check that HTTPS is working

### 4. Troubleshooting
- **DNS not working**: Wait 24-48 hours for propagation
- **HTTPS issues**: Enable "Enforce HTTPS" in GitHub Pages settings
- **CNAME conflicts**: Make sure no other CNAME records exist

## Current Status
✅ CNAME file created in repository
⏳ DNS configuration needed
⏳ GitHub Pages settings verification needed

# Google Sheets Template for Om Handicraft

## Sheet Structure

Create a Google Sheet with the following columns:

| Column A | Column B | Column C | Column D | Column E | Column F | Column G |
|----------|----------|----------|----------|----------|----------|----------|
| **product_id** | **name** | **category** | **size** | **price** | **availability** | **note** |

## Column Descriptions

- **product_id**: Unique identifier for each product (e.g., pottery-001, textile-002)
- **name**: Product name (e.g., "Handmade Ceramic Bowl")
- **category**: Product category (e.g., "Pottery", "Textiles", "Woodwork")
- **size**: Size variant (e.g., "Small", "Medium", "Large", "Standard")
- **price**: Price in rupees (e.g., 450, 650)
- **availability**: Stock status (e.g., "In Stock", "Limited Stock", "Out of Stock")
- **note**: Additional description or notes

## Sample Data

| product_id | name | category | size | price | availability | note |
|------------|------|----------|------|-------|--------------|------|
| pottery-001 | Handmade Ceramic Bowl | Pottery | Medium | 450 | In Stock | Beautiful handcrafted ceramic bowl perfect for serving |
| pottery-002 | Handmade Ceramic Bowl | Pottery | Large | 650 | In Stock | Beautiful handcrafted ceramic bowl perfect for serving |
| textile-001 | Embroidered Cushion Cover | Textiles | Standard | 350 | In Stock | Intricately embroidered cushion cover |
| wood-001 | Carved Wooden Box | Woodwork | Small | 800 | Limited Stock | Hand-carved wooden jewelry box |

## Image Naming Convention

- Images should be stored in Google Drive
- Image filename should match the product_id exactly
- Supported formats: .jpg, .jpeg, .png
- Example: pottery-001.jpg, textile-002.png

## Instructions for Non-Tech Users

1. **Adding New Products**: Simply add a new row with all required information
2. **Updating Products**: Edit the existing row with new information
3. **Removing Products**: Delete the entire row
4. **Adding Images**: Upload image to Google Drive with the exact product_id as filename
5. **Categories**: Use consistent category names (Pottery, Textiles, Woodwork, etc.)

## Automation

The Python script will automatically:
- Read this Google Sheet
- Download images from Google Drive
- Update the website with new products
- Generate the products.json file
- Update category filters

No technical knowledge required - just update the sheet and images!

// Om Handicraft Website JavaScript
class OmHandicraft {
    constructor() {
        this.products = [];
        this.categories = [];
        this.currentCategory = 'all';
        this.init();
    }

    async init() {
        await this.loadProducts();
        this.setupEventListeners();
        this.renderCategories();
        this.renderProducts();
    }

    async loadProducts() {
        try {
            // In production, this would fetch from your generated data file
            // For now, using sample data
            const response = await fetch('data/products.json');
            if (response.ok) {
                const data = await response.json();
                this.products = data.products || [];
                this.categories = data.categories || [];
            } else {
                // Fallback to sample data if file doesn't exist
                this.loadSampleData();
            }
        } catch (error) {
            console.log('Using sample data for development');
            this.loadSampleData();
        }
    }

    loadSampleData() {
        this.products = [
            {
                id: 'pottery-001',
                name: 'Handmade Ceramic Bowl',
                category: 'Pottery',
                size: 'Medium',
                price: 450,
                availability: 'In Stock',
                image: 'pottery-001.jpg',
                note: 'Beautiful handcrafted ceramic bowl perfect for serving'
            },
            {
                id: 'pottery-002',
                name: 'Handmade Ceramic Bowl',
                category: 'Pottery',
                size: 'Large',
                price: 650,
                availability: 'In Stock',
                image: 'pottery-002.jpg',
                note: 'Beautiful handcrafted ceramic bowl perfect for serving'
            },
            {
                id: 'textile-001',
                name: 'Embroidered Cushion Cover',
                category: 'Textiles',
                size: 'Standard',
                price: 350,
                availability: 'In Stock',
                image: 'textile-001.jpg',
                note: 'Intricately embroidered cushion cover'
            },
            {
                id: 'wood-001',
                name: 'Carved Wooden Box',
                category: 'Woodwork',
                size: 'Small',
                price: 800,
                availability: 'Limited Stock',
                image: 'wood-001.jpg',
                note: 'Hand-carved wooden jewelry box'
            }
        ];

        this.categories = ['Pottery', 'Textiles', 'Woodwork'];
    }

    setupEventListeners() {
        // Category filter buttons
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('category-filter')) {
                this.handleCategoryFilter(e.target);
            }
        });
    }

    handleCategoryFilter(button) {
        // Remove active class from all buttons
        document.querySelectorAll('.category-filter').forEach(btn => {
            btn.classList.remove('active', 'bg-amber-500', 'text-white');
            btn.classList.add('bg-white');
        });

        // Add active class to clicked button
        button.classList.add('active', 'bg-amber-500', 'text-white');
        button.classList.remove('bg-white');

        this.currentCategory = button.dataset.category;
        this.renderProducts();
    }

    renderCategories() {
        const container = document.querySelector('.flex.flex-wrap.gap-2.justify-center');
        
        // Add category buttons
        this.categories.forEach(category => {
            const button = document.createElement('button');
            button.className = 'category-filter px-6 py-3 rounded-full bg-white shadow-md hover:shadow-lg transition-all duration-300 hover-lift';
            button.dataset.category = category;
            button.textContent = category;
            container.appendChild(button);
        });
    }

    renderProducts() {
        const container = document.getElementById('products-container');
        const loading = document.getElementById('loading');
        const emptyState = document.getElementById('empty-state');

        // Hide loading
        loading.style.display = 'none';

        // Filter products based on category
        const filteredProducts = this.currentCategory === 'all' 
            ? this.products 
            : this.products.filter(product => product.category === this.currentCategory);

        // Show empty state if no products
        if (filteredProducts.length === 0) {
            emptyState.classList.remove('hidden');
            container.innerHTML = '';
            return;
        }

        // Hide empty state
        emptyState.classList.add('hidden');

        // Render products
        container.innerHTML = filteredProducts.map(product => this.createProductCard(product)).join('');
    }

    createProductCard(product) {
        const availabilityColor = product.availability === 'In Stock' ? 'text-green-600' : 
                                 product.availability === 'Limited Stock' ? 'text-yellow-600' : 'text-red-600';

        return `
            <div class="product-card bg-white rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 hover-lift fade-in overflow-hidden">
                <div class="relative">
                    <img src="images/${product.image}" 
                         alt="${product.name}" 
                         class="w-full h-64 object-cover"
                         onerror="this.src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZjNmNGY2Ii8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzk5YTNhZiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPkltYWdlIG5vdCBmb3VuZDwvdGV4dD48L3N2Zz4='">
                    <div class="absolute top-4 right-4">
                        <span class="px-3 py-1 rounded-full text-sm font-medium ${availabilityColor} bg-white/90 backdrop-blur-sm">
                            ${product.availability}
                        </span>
                    </div>
                </div>
                <div class="p-6">
                    <h3 class="text-xl font-semibold text-gray-800 mb-2">${product.name}</h3>
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-sm text-gray-600">Size: ${product.size}</span>
                        <span class="text-2xl font-bold text-amber-600">₹${product.price}</span>
                    </div>
                    <p class="text-gray-600 text-sm mb-4">${product.note}</p>
                    <button class="w-full bg-amber-500 hover:bg-amber-600 text-white font-semibold py-3 px-4 rounded-lg transition-colors duration-300 flex items-center justify-center space-x-2">
                        <i class="fab fa-whatsapp"></i>
                        <span>Contact for Order</span>
                    </button>
                </div>
            </div>
        `;
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new OmHandicraft();
});

def recommend_product(product_type, budget):
    products = {
        "tv": [
            {"name": "Smart TV", "description": "A modern Smart TV for home entertainment.", "price": 3500},
            {"name": "43-inch Smart TV", "description": "A 43-inch Smart TV suitable for home entertainment.", "price": 4500},
            {"name": "55-inch Smart TV", "description": "A larger Smart TV suitable for movies and sports.", "price": 6500},
        ],
        "laptop": [
            {"name": "HP Laptop", "description": "Suitable for school and office work.", "price": 4500},
            {"name": "Dell Laptop", "description": "Suitable for business and everyday computing.", "price": 5500},
            {"name": "Lenovo Laptop", "description": "Suitable for students and productivity.", "price": 5000},
        ],
        "phone": [
            {"name": "Android Smartphone", "description": "Affordable smartphone for everyday use.", "price": 1800},
            {"name": "Mid-range Smartphone", "description": "Good performance, camera and battery life.", "price": 3000},
            {"name": "Premium Smartphone", "description": "High-performance smartphone with advanced features.", "price": 5500},
        ],
        "fridge": [
            {"name": "Single Door Refrigerator", "description": "Compact refrigerator suitable for smaller households.", "price": 3000},
            {"name": "Double Door Refrigerator", "description": "Larger refrigerator suitable for families.", "price": 5000},
            {"name": "Large Family Refrigerator", "description": "Large-capacity refrigerator for bigger households.", "price": 7000},
        ],
    }

    product_list = products.get(product_type, [])
    affordable = [p for p in product_list if p["price"] <= budget]

    if not affordable:
        return f"I couldn't find a {product_type} within GHS {budget:,} in my demo catalogue. Would you like to increase your budget?"

    best = affordable[-1]
    return (
        f"💡 Based on your budget of GHS {budget:,}, I recommend the {best['name']}.\n\n"
        f"Description: {best['description']}\n"
        f"Demo price: GHS {best['price']:,}\n\n"
        "Note: These are sample/demo prices, not verified current Melcom prices."
    )

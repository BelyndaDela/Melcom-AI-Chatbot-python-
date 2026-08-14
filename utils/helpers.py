def recommend_product(product_type, budget):
    products = {
        "tv": [
            {
                "name": "Budget Smart TV",
                "price": 2500,
                "description": "A smart TV suitable for everyday home entertainment."
            },
            {
                "name": "Mid-Range Smart TV",
                "price": 4000,
                "description": "A larger smart TV with good features for families."
            },
            {
                "name": "Premium Smart TV",
                "price": 6500,
                "description": "A premium TV with advanced features and a larger display."
            },
        ],

        "laptop": [
            {
                "name": "Basic Laptop",
                "price": 3000,
                "description": "Suitable for browsing, documents and school work."
            },
            {
                "name": "Mid-Range Laptop",
                "price": 5000,
                "description": "Suitable for programming, business and general productivity."
            },
            {
                "name": "Performance Laptop",
                "price": 7500,
                "description": "Suitable for demanding applications and heavier workloads."
            },
        ],

        "phone": [
            {
                "name": "Budget Smartphone",
                "price": 1500,
                "description": "An affordable smartphone for everyday use."
            },
            {
                "name": "Mid-Range Smartphone",
                "price": 3000,
                "description": "A balanced smartphone for communication, apps and entertainment."
            },
            {
                "name": "Premium Smartphone",
                "price": 6000,
                "description": "A high-end smartphone with advanced features."
            },
        ],

        "fridge": [
            {
                "name": "Compact Refrigerator",
                "price": 2500,
                "description": "A compact refrigerator suitable for smaller households."
            },
            {
                "name": "Family Refrigerator",
                "price": 4500,
                "description": "A larger refrigerator suitable for a family."
            },
            {
                "name": "Large Premium Refrigerator",
                "price": 7000,
                "description": "A large refrigerator with additional storage and features."
            },
        ],
    }

    product_list = products.get(product_type, [])

    if not product_list:
        return (
            "I don't currently have a recommendation for that product category. "
            "Please try asking about a TV, laptop, phone or refrigerator."
        )

    affordable = [
        product for product in product_list
        if product["price"] <= budget
    ]

    if not affordable:
        cheapest = min(product_list, key=lambda product: product["price"])

        return (
            f"I couldn't find a {product_type} within a budget of GH₵{budget:,}. "
            f"The most affordable option in my sample catalogue is "
            f"{cheapest['name']} at approximately GH₵{cheapest['price']:,}."
        )

    recommended = max(
        affordable,
        key=lambda product: product["price"]
    )

    return (
        f"Based on your budget of GH₵{budget:,}, I recommend "
        f"{recommended['name']} at approximately "
        f"GH₵{recommended['price']:,}. "
        f"{recommended['description']}"
    )
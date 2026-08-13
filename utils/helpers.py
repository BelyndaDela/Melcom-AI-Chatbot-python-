def recommend_product(product_type, budget):
    products = {
        "tv": "We recommend checking our available TVs based on your budget and preferred screen size.",
        "laptop": "We recommend choosing a laptop based on your intended use, specifications, and budget.",
        "phone": "We recommend comparing smartphones based on brand, storage, camera, battery, and budget.",
        "fridge": "We recommend choosing a refrigerator based on capacity, energy efficiency, features, and budget."
    }

    message = products.get(
        product_type,
        "Please tell me the product you are looking for."
    )

    return f"{message} Your stated budget is GHS {budget:,}."

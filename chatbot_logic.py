from utils.helpers import recommend_product

def fallback_response():
    return (
        "I'm sorry, I couldn't understand your question. "
        "I can help with products, recommendations, orders, delivery, "
        "returns, refunds, payments, and Melcom branches. What would you like help with?"
    )

def greeting_response():
    return "Hello! 👋 Welcome to Melcom Ghana. I'm your Melcom AI Assistant. How can I help you today?"

def product_assistant(query):
    query = query.lower()

    if "tv" in query or "television" in query:
        return "📺 We can help you find a TV based on your budget and preferred screen size. What is your budget?"
    if "laptop" in query or "computer" in query:
        return "💻 We can help you find a laptop for school, office work, programming, business, or gaming. What will you use it for?"
    if "phone" in query or "smartphone" in query or "mobile" in query:
        return "📱 We can help you find a smartphone. Tell me your preferred brand or budget."
    if "fridge" in query or "refrigerator" in query:
        return "🧊 We can help you choose a refrigerator. What is your budget and preferred size?"
    if "furniture" in query or "sofa" in query or "chair" in query:
        return "🛋️ We can help you find furniture. Are you looking for a sofa, chair, table, bed, or another item?"
    if "washing machine" in query:
        return "🧺 We can help you choose a washing machine. Tell me your budget and preferred capacity."
    if "microwave" in query:
        return "🍽️ We can help you find a microwave oven. What is your preferred budget?"

    return "Please tell me the product you are looking for, such as a TV, phone, laptop, refrigerator, or furniture."

def recommendation_response(query):
    query = query.lower()
    budget = 5000

    for word in query.replace(",", "").split():
        if word.isdigit():
            budget = int(word)
            break

    if "tv" in query or "television" in query:
        product_type = "tv"
    elif "laptop" in query or "computer" in query:
        product_type = "laptop"
    elif "phone" in query or "smartphone" in query:
        product_type = "phone"
    elif "fridge" in query or "refrigerator" in query:
        product_type = "fridge"
    else:
        return "Tell me the product and budget. Example: 'Recommend a TV under 5000'."

    return recommend_product(product_type, budget)

def customer_service(query):
    if "return" in query:
        return "🔄 For a return, keep the item in its original condition and packaging. Please contact Melcom support or the relevant branch to confirm the applicable return procedure."
    if "refund" in query:
        return "💰 For a refund request, keep your receipt or order details and contact Melcom customer support for the applicable procedure."
    if "damaged" in query or "damage" in query:
        return "⚠️ If your product arrived damaged, keep the product, packaging and proof of purchase, then contact Melcom support or the relevant branch."
    if "exchange" in query:
        return "🔄 For an exchange, keep your receipt and the product in its original condition. Melcom staff can confirm eligibility."
    return "I can help with returns, refunds, damaged products and exchanges. Please tell me what happened."

def store_info():
    return "🏪 Melcom has branches across Ghana. For current branch addresses, opening hours and services, please check Melcom's official channels."

def delivery_info():
    return "🚚 I can help with delivery questions. To track an order, please provide your order number."

def payment_info():
    return "💳 For payment questions, please check the payment options shown during checkout or contact Melcom customer support for the latest information."

def order_info(query):
    if "cancel" in query:
        return "❌ If you want to cancel an order, contact Melcom customer support as soon as possible. Cancellation may depend on the order status."
    return "📦 I can help with your order. Please provide your order number and tell me what you need help with."

def handle_query(user_input, context=None):
    if context is None:
        context = {}

    if not user_input:
        return "Please type a question so I can help you."

    query = user_input.lower().strip()

    greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
    if any(query == g or query.startswith(g + " ") for g in greetings):
        return greeting_response()

    if "thank you" in query or "thanks" in query:
        return "You're very welcome! 😊 Is there anything else you would like to know about Melcom?"

    product_words = [
        "tv", "television", "phone", "smartphone", "mobile", "laptop", "computer",
        "fridge", "refrigerator", "furniture", "sofa", "chair", "washing machine", "microwave"
    ]
    if any(word in query for word in product_words):
        if "recommend" in query or "best" in query or "budget" in query:
            return recommendation_response(query)
        return product_assistant(query)

    if any(word in query for word in ["recommend", "recommendation", "what should i buy", "which one should i buy"]):
        return recommendation_response(query)

    if any(word in query for word in ["return", "refund", "damaged", "damage", "exchange"]):
        return customer_service(query)

    if any(word in query for word in ["branch", "branches", "store", "location", "shop"]):
        return store_info()

    if any(word in query for word in ["delivery", "deliver", "shipping"]):
        return delivery_info()

    if any(word in query for word in ["order", "track", "tracking", "cancel order"]):
        return order_info(query)

    if any(word in query for word in ["payment", "pay", "cash", "card", "momo", "mobile money"]):
        return payment_info()

    if "help" in query or "what can you do" in query:
        return (
            "🤖 I can help with:\n\n"
            "📺 Products and product information\n"
            "💰 Product recommendations\n"
            "📦 Orders and tracking\n"
            "🚚 Delivery questions\n"
            "🔄 Returns and refunds\n"
            "🏪 Melcom branches\n"
            "💳 Payment questions"
        )

    return fallback_response()

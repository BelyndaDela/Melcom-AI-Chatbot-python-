import re
from utils.helpers import recommend_product


def handle_query(user_input, context=None):
    """
    Main chatbot logic.
    """

    if context is None:
        context = {}

    if not user_input:
        return "Please type a message so I can help you."

    message = user_input.strip()
    text = message.lower()

    # Remember user's name
    name_match = re.search(
        r"\bmy name is\s+([a-zA-Z]+)",
        message,
        re.IGNORECASE
    )

    if name_match:
        name = name_match.group(1).capitalize()
        context["name"] = name

        return (
            f"Nice to meet you, {name}! 👋 "
            "I'm your Melcom AI Assistant. "
            "How can I help you today?"
        )

    # Greeting
    greeting_words = [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    if any(word in text for word in greeting_words):
        name = context.get("name")

        if name:
            return (
                f"Hello again, {name}! 👋 "
                "How can I help you today?"
            )

        return (
            "Hello! 👋 Welcome to Melcom Ghana. "
            "I'm your Melcom AI Assistant. "
            "How can I help you today?"
        )

    # Thank you
    if any(word in text for word in [
        "thank you",
        "thanks",
        "thank"
    ]):
        return (
            "You're very welcome! 😊 "
            "I'm happy to help."
        )

    # Goodbye
    if any(word in text for word in [
        "bye",
        "goodbye",
        "see you"
    ]):
        return (
            "Goodbye! 👋 Thank you for using the "
            "Melcom AI Assistant."
        )

    # Recommendation requests
    recommendation_words = [
        "recommend",
        "recommendation",
        "recommentation",
        "recomendation",
        "suggest",
        "suggestion",
        "best",
        "which one",
        "what should i buy"
    ]

    if any(word in text for word in recommendation_words):

        # TV
        if any(word in text for word in [
            "tv",
            "television",
            "smart tv"
        ]):

            budget = extract_budget(text)

            if budget:
                return recommend_product("tv", budget)

            return (
                "📺 I can help you choose a TV. "
                "What is your budget in Ghana cedis?"
            )

        # Laptop
        if any(word in text for word in [
            "laptop",
            "computer",
            "notebook"
        ]):

            budget = extract_budget(text)

            if budget:
                return recommend_product("laptop", budget)

            return (
                "💻 I can help you find a laptop for "
                "school, office work, programming, business, "
                "or gaming. What is your budget?"
            )

        # Phone
        if any(word in text for word in [
            "phone",
            "smartphone",
            "mobile"
        ]):

            budget = extract_budget(text)

            if budget:
                return recommend_product("phone", budget)

            return (
                "📱 I can help you choose a smartphone. "
                "What is your budget?"
            )

        # Refrigerator
        if any(word in text for word in [
            "fridge",
            "refrigerator"
        ]):

            budget = extract_budget(text)

            if budget:
                return recommend_product("fridge", budget)

            return (
                "❄️ I can help you choose a refrigerator. "
                "What is your budget?"
            )

    # Direct product + budget requests
    budget = extract_budget(text)

    if budget:

        if any(word in text for word in [
            "tv",
            "television",
            "smart tv"
        ]):
            return recommend_product("tv", budget)

        if any(word in text for word in [
            "laptop",
            "computer",
            "notebook"
        ]):
            return recommend_product("laptop", budget)

        if any(word in text for word in [
            "phone",
            "smartphone",
            "mobile"
        ]):
            return recommend_product("phone", budget)

        if any(word in text for word in [
            "fridge",
            "refrigerator"
        ]):
            return recommend_product("fridge", budget)

    # Laptop
    if any(word in text for word in [
        "laptop",
        "computer",
        "notebook"
    ]):
        return (
            "💻 I can help you find a laptop for "
            "school, office work, programming, business, "
            "or gaming. What is your budget?"
        )

    # Delivery
    if any(word in text for word in [
        "delivery",
        "deliver",
        "shipping",
        "ship"
    ]):
        return (
            "📦 Melcom offers delivery services for selected "
            "orders and locations. Please provide your order "
            "details or location so we can determine the "
            "appropriate delivery information."
        )

    # Orders
    if any(word in text for word in [
        "order",
        "orders",
        "track my order",
        "order status"
    ]):
        return (
            "📦 I can help with order enquiries. "
            "Please provide your order number or the details "
            "of the product you ordered."
        )

    # Returns and refunds
    if any(word in text for word in [
        "return",
        "returns",
        "refund",
        "refunds",
        "exchange",
        "exchanges"
    ]):
        return (
            "🔄 I can help with returns, refunds, and exchanges. "
            "Please provide details about the product and "
            "your order."
        )

    # Payments
    if any(word in text for word in [
        "payment",
        "payments",
        "pay",
        "cash",
        "card",
        "mobile money",
        "momo"
    ]):
        return (
            "💳 I can help with payment enquiries. "
            "Please tell me which payment method you would "
            "like to know about."
        )

    # Branches
    if any(word in text for word in [
        "branch",
        "branches",
        "store",
        "stores",
        "location",
        "locations"
    ]):
        return (
            "🏪 Melcom has branches in different locations "
            "across Ghana. Tell me the city or area you are "
            "looking for, and I can help you with the branch enquiry."
        )

    # Products
    if any(word in text for word in [
        "product",
        "products",
        "items",
        "sell",
        "selling"
    ]):
        return (
            "🛍️ Melcom offers a wide range of products, "
            "including electronics, appliances, furniture, "
            "phones, computers, home products, and more."
        )

    # Help
    if any(word in text for word in [
        "help",
        "what can you do",
        "what do you do"
    ]):
        return (
            "🤖 I can help you with:\n\n"
            "🛍️ Product information\n"
            "💰 Product recommendations\n"
            "📦 Orders and delivery\n"
            "🔄 Returns and refunds\n"
            "💳 Payments\n"
            "🏪 Melcom branches\n\n"
            "What would you like to know?"
        )

    # Fallback
    return (
        "I'm sorry, I couldn't understand your question. "
        "I can help with products, recommendations, orders, "
        "delivery, returns, refunds, payments, and Melcom branches. "
        "What would you like help with?"
    )


def extract_budget(text):
    """
    Extract a budget from messages such as:

    5000
    5,000
    GH₵5000
    GHS 5000
    under 5000
    below 5000
    budget 5000
    """

    patterns = [
        r"gh₵\s*([\d,]+)",
        r"ghs\s*([\d,]+)",
        r"₵\s*([\d,]+)",
        r"budget\s*(?:of|is)?\s*([\d,]+)",
        r"(?:under|below|less than|up to)\s*(?:gh₵|ghs|₵)?\s*([\d,]+)",
        r"([\d,]+)\s*(?:gh₵|ghs|₵)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            try:
                return int(match.group(1).replace(",", ""))
            except ValueError:
                pass

    return None

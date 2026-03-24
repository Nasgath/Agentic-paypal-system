import requests

# -----------------------
# Use the sandbox access token you provided
ACCESS_TOKEN = "A21AAJt-Hseuwjha8Lhss-HH2QTEwys1XvMPer9dKro0Q59KyBRZIg66WwPl1V4ugnKSY_siE7Aile6k926NkWVUeuhpsUOKg"
# -----------------------

# PAYPAL TOOLS
def create_order(amount):
    url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    data = {
        "intent": "CAPTURE",
        "purchase_units": [
            {"amount": {"currency_code": "USD", "value": str(amount)}}
        ]
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()


def capture_payment(order_id):
    url = f"https://api-m.sandbox.paypal.com/v2/checkout/orders/{order_id}/capture"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.post(url, headers=headers)
    return response.json()


# -----------------------
# Simple Intent Router
def route(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["pay", "payment"]):
        return "payment"
    elif any(word in user_input for word in ["what", "info", "explain"]):
        return "rag"
    elif any(word in user_input for word in ["tool", "status"]):
        return "system"
    return "unknown"


# -----------------------
# AGENT FUNCTION
def agent(user_input):
    intent = route(user_input)

    if intent == "payment":
        print("Intent: Payment detected")
        order = create_order(50)  # Example: $50
        print("Order Response:", order)
        if "id" in order:
            capture_resp = capture_payment(order["id"])
            return {"order": order, "capture": capture_resp}
        else:
            return {"error": "Order creation failed", "details": order}

    elif intent == "rag":
        return "RAG Tool: Fetching information..."

    elif intent == "system":
        return "System Tool: Available tools -> Payment, RAG, System"

    return "Not understood"


# -----------------------
# RUN AGENT
if __name__ == "__main__":
    user = input("Enter request: ")
    result = agent(user)
    print(result)
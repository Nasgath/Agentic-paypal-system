from router import route
from tools.paypal import create_order, capture_payment
from config import TOOLS

def agent(user_input):
    intent = route(user_input)

    if intent == "payment":
        selected_tools = TOOLS["payment"]
        print("Selected Tools:", selected_tools)

        order = create_order(50)
        result = capture_payment(order["id"])
        return result

    elif intent == "rag":
        return "RAG Tool: Fetching information..."

    elif intent == "system":
        return "System Tool: Available tools -> Payment, RAG, System"

    return "Not understood"


if __name__ == "__main__":
    user = input("Enter request: ")
    print(agent(user))
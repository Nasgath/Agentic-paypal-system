def route(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["pay", "payment"]):
        return "payment"
    elif any(word in user_input for word in ["what", "explain"]):
        return "rag"
    elif any(word in user_input for word in ["tool", "status"]):
        return "system"

    return "unknown"
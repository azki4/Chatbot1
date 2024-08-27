
#Written by: Azkiya Tahreem

def chatbot_response(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I help you today?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that."

# Example usage
user_input = input("You: ")
print("Chatbot:", chatbot_response(user_input))


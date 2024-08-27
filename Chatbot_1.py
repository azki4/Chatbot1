
#Written by: Azkiya Tahreem

import tkinter as tk

def chatbot_response(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I help you today?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that."

def send_message():
    user_input = user_input_entry.get()
    chatbox.insert(tk.END, "You: " + user_input + "\n")
    chatbox.insert(tk.END, "Chatbot: " + chatbot_response(user_input) + "\n")
    user_input_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Interactive Chatbot")

# Create the chatbox
chatbox = tk.Text(root, height=20, width=50)
chatbox.pack()

# Create the user input entry
user_input_entry = tk.Entry(root, width=40)
user_input_entry.pack(side=tk.LEFT, padx=10)

# Create the send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

# Run the main loop
root.mainloop()

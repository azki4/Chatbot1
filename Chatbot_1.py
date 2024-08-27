
#Written by: Azkiya Tahreem

import tkinter as tk
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_response(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I help you today?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

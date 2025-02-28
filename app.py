from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Add it to the .env file.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask server is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = model.generate_content(user_message)
    return jsonify({"reply": response.text if response else "Sorry, I couldn't process that."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Use Render's port

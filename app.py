from flask import Flask, request, jsonify, render_template
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Load the model and tokenizer once
model_name = "microsoft/DialoGPT-medium"  # Use a smaller model if possible
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Use GPU if available
device = 0 if torch.cuda.is_available() else -1

chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer, device=device)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    response = chatbot(user_message, max_length=100, num_return_sequences=1, truncation=True)
    return jsonify({"response": response[0]['generated_text']})

if __name__ == "__main__":
    app.run(debug=True)

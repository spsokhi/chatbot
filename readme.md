# NLP Chatbot

This is an NLP Chatbot application using Flask and DialoGPT. The chatbot is served using Gunicorn for improved performance and can handle multiple user requests efficiently.

## File Structure
```
├── app.py                  # Main application file
├── requirements.txt        # Python dependencies
├── static
│   └── style.css           # CSS for styling the frontend
├── templates
│   └── index.html          # HTML template for the frontend
└── README.md               # This README file
```
## Features
- Interactive chatbot using the `microsoft/DialoGPT-large` model.
- Modern and responsive UI with CSS animations.
- Marquee text for welcoming users.
- Loading indicator to show processing status.

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/spsokhi/chatbot.git
   cd chatbot
2. **Create and activate a virtual environment**:
    ```
    python3 -m venv chatbot_env
    source chatbot_env/bin/activate  # On Windows use `chatbot_env\Scripts\activate`
3. **Install dependencies**:
    ```
    pip install -r requirements.txt


## Running the Application
1. **Start the Gunicorn server**:
    ```
    gunicorn -w 2 -b 127.0.0.1:5000 app:app
2. **Open your browser and navigate to http://127.0.0.1:5000 to access the chatbot.**


## Using Different Models
**You can use various models available on the Hugging Face Model Hub. Here are some models you can experiment with:**

1. **DialoGPT Models**
   + microsoft/DialoGPT-small
   + microsoft/DialoGPT-medium
   + microsoft/DialoGPT-large
2. **GPT-2 Models**
   + gpt2
   + gpt2-medium
   + gpt2-large
   + gpt2-xl
3. **T5 Models**
   + t5-small
   + t5-base
   + t5-large
4. **BERT Variants (for understanding-based tasks)**
   + bert-base-uncased
   + distilbert-base-uncased
5. **Other Conversational Models**
   + facebook/blenderbot-400M-distill
   + facebook/blenderbot-1B-distill
   + microsoft/GODEL-v1_1-base-seq2seq
   + microsoft/GODEL-v1_1-large-seq2seq

## Changing the Model
**To change the model, update the following line in app.py:**
   ```
 model_name = "microsoft/DialoGPT-medium"  # Change this to the desired model
   ```
**For example, to use the facebook/blenderbot-400M-distill model, update the line to:**
   ```
   model_name = "facebook/blenderbot-400M-distill"
   ```



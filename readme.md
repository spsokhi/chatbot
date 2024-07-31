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
   git clone <repository-url>
   cd <repository-directory>
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


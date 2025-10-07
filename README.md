# 🧠 AI Text Generator (Sentiment-Based)

This project is a **Flask-based web app** that generates AI text aligned with a chosen or automatically detected **sentiment (positive, negative, neutral)**.  
It uses **TextBlob** for sentiment detection and **Hugging Face Transformers (GPT-2 family)** for text generation.

---

## 🚀 Features

✅ Generate AI text from a user prompt  
✅ Automatically detect sentiment or choose one manually  
✅ Choose between **GPT-2** and **GPT-2-Medium** models  
✅ Adjustable text length  
✅ Stylish, responsive web UI  
✅ Real-time preview of generated output  

---

## 🏗️ Project Structure

### AI-Text-Generator/
### │
### ├── app.py # Main Flask app (handles routes & logic)
### ├── utils.py # Helper functions for sentiment & generation
### ├── templates/
### │ └── index.html # Main HTML page
### ├── static/
### │ └── style.css # Stylesheet for UI
### ├── requirements.txt # Dependencies
### └── README.md # Project documentation


Quick start

## 1. Create a virtual environment (recommended): 
python -m venv venv source 
venv/bin/activate   # macOS / Linux 
venv\Scripts\activate     # Windows

## 2. Install requirements: pip install -r requirements.txt

## 3. Run the app: python app.py







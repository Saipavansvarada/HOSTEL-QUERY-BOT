# HOSTEL-QUERY-BOT

A **Hostel Query Bot** that answers FAQs about Hostel using **Python, Flask, and TF-IDF NLP**.  
Users can ask questions about events , check-in/out and number of people via a web interface.

---

## **Live Demo**

[http://127.0.0.1:5000/]  

---

## **Tech Stack**

- **Python 3**
- **Flask** – Backend web framework
- **scikit-learn** – TF-IDF vectorization & cosine similarity
- **NumPy** – Array operations and scoring
- **HTML / JavaScript** – Frontend interface
- **Render / Heroku** – Deployment

---

## **Project Structure**

HostelChatbot/
─ app.py # Backend Flask app
─ faqs.json # FAQ dataset
─ requirements.txt # Python dependencies
─ templates/
  ── index.html # Frontend page
─ static/
─ script.js # JavaScript logic
  

# Usage

Enter your question in the input box.

Click Ask.

The bot will return the most relevant FAQ answer.

If no answer is confident, it suggests contacting the admin.

# How It Works

The user question is sent from the browser to Flask backend.

TF-IDF vectorization and cosine similarity find the closest matching FAQ.

The best answer is returned to the frontend.

# Future Improvements

Integrate OpenAI GPT / RAG for conversational answers.

Add login system for personalized queries.

Analytics for most asked questions.

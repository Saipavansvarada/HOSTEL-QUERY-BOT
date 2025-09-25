from flask import Flask, request, jsonify, render_template
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)

# 1. Load FAQs from JSON
with open("faqs.json", "r", encoding="utf-8") as f:
    FAQS = json.load(f)

QUESTIONS = [item["question"] for item in FAQS]

# 2. Build TF-IDF index
vectorizer = TfidfVectorizer().fit(QUESTIONS)
Q_VECTORS = vectorizer.transform(QUESTIONS)

# 3. Function to find best FAQ match
def retrieve_best_answer(query, top_k=3):
    q_vec = vectorizer.transform([query])
    sims = cosine_similarity(q_vec, Q_VECTORS)[0]
    top_idx = np.argsort(sims)[::-1][:top_k]
    results = []
    for idx in top_idx:
        results.append({
            "id": FAQS[idx]["id"],
            "question": FAQS[idx]["question"],
            "answer": FAQS[idx]["answer"],
            "score": float(sims[idx])
        })
    return results

# 4. Home route to serve frontend
@app.route("/")
def home():
    return render_template("index.html")

# 5. API endpoint for questions
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    q = data.get("question", "").strip()
    if not q:
        return jsonify({"error": "No question provided"}), 400

    results = retrieve_best_answer(q, top_k=3)

    # Threshold to handle unknown questions
    if results[0]["score"] < 0.2:
        return jsonify({
            "answer": "Sorry, I couldn’t find an answer. Please contact admin.",
            "candidates": results
        })

    return jsonify({
        "answer": results[0]["answer"],
        "candidates": results
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)


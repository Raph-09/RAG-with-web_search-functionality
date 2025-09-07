from flask import Flask, request, jsonify, render_template
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()
from src.agent import llm, search_tool, chain



app = Flask(__name__)

# ------------------- FRONTEND -------------------
@app.route("/")
def home():
    return render_template("index.html")

# ------------------- API ENDPOINT -------------------
@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        question = data.get("question", "").strip()

        if not question:
            return jsonify({"answer": "⚠️ Please provide a valid question."})

        # 🔎 Search Tavily
        search_results = search_tool.run(question)

        # 🧠 Generate answer with context
        answer = chain.run({"context": search_results, "question": question})

        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"answer": f"🚨 Error: {str(e)}"}), 500

# ------------------- MAIN -------------------
if __name__ == "__main__":
    app.run(debug=True)

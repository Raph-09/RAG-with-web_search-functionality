# RAG with Web Search – Flask, LangChain, Groq & Tavily

## 📌 Overview

This project implements a Retrieval-Augmented Generation (RAG) application that integrates Groq LLM with Tavily web search API using LangChain, exposed through a Flask backend and a lightweight HTML/CSS frontend.

The application allows users to ask questions in natural language. The system performs a web search using Tavily, retrieves relevant context, and generates accurate responses with Groq.

The solution is containerized with Docker and includes a GitHub Actions CI/CD pipeline that builds and publishes the Docker image to DockerHub.

## ⚙️Features

RAG pipeline: Combines Groq LLM with Tavily search results for contextual answers.

Flask REST API: /ask endpoint to handle user queries.

Frontend UI: Simple web interface built with HTML, CSS, and JavaScript.

Postman/cURL Testing: API can be tested directly with JSON requests.

Dockerized: Runs seamlessly inside a container.

CI/CD with GitHub Actions: Automatically builds and pushes images to DockerHub.

## 🚀 Getting Started
1. Clone Repository
git clone https://github.com/<your-username>/rag-websearch.git
cd rag-websearch

2. Set Environment Variables

Create a .env file or set in shell:

export GROQ_API_KEY=your_groq_api_key
export TAVILY_API_KEY=your_tavily_api_key

3. Install Dependencies
pip install -r requirements.txt

4. Run Flask App
python app.py


The app will be available at: http://127.0.0.1:5000

## 🌐 Usage
Frontend

Open http://127.0.0.1:5000 in a browser, type a question, and view the answer.

API (cURL)
curl -X POST http://127.0.0.1:5000/ask \
     -H "Content-Type: application/json" \
     -d '{"question": "What is Retrieval-Augmented Generation?"}'


Expected response:

{
  "answer": "Retrieval-Augmented Generation (RAG) is..."
}

## 🐳 Docker Setup
Build Image
docker build -t rag-websearch .

Run Container
docker run -p 5000:5000 -e GROQ_API_KEY=your_key -e TAVILY_API_KEY=your_key rag-websearch

⚡ CI/CD with GitHub Actions

This project includes a GitHub Actions workflow (.github/workflows/docker-publish.yml) that:

Builds the Docker image.

Logs in to DockerHub.

Pushes the image to your DockerHub repository.

Setup

Add GitHub secrets:

DOCKERHUB_USERNAME

DOCKERHUB_TOKEN

Every push to main triggers a build & publish.

## 🛠️ Tech Stack

Backend: Flask, LangChain

LLM: Groq

Search API: Tavily

Frontend: HTML, CSS, JavaScript

Containerization: Docker

CI/CD: GitHub Actions + DockerHub

## ✅ Future Improvements

Add vector database support (e.g., Pinecone, Weaviate, FAISS).

Enhance UI with React or Vue.

Add user authentication.

Implement caching for faster responses.

👨‍💻 Author

Developed by Abasiama Raphael Akpan.
Feel free to contribute or raise issues! 🚀

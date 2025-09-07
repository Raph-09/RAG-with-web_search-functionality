from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.config import settings
import os
load_dotenv()

# Groq LLM wrappe

llm = ChatGroq(
    groq_api_key=settings.GROQ_API_KEY,
    model=settings.model,   # ✅ change if you want llama3 etc.
    temperature=0.3
)

# Tavily search tool
search_tool = TavilySearchResults(tavily_api_key=settings.TAVILY_API_KEY)

# Prompt template
prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant. Use the following web search results if relevant:

Search Results:
{context}

Now, answer the user query:
{question}
""")

# Chain setup
chain = LLMChain(llm=llm, prompt=prompt)
from urllib.parse import quote_plus
from dotenv import load_dotenv
import requests
import os
from fastapi import FastAPI, HTTPException
from bs4 import BeautifulSoup
import ollama
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage
from datetime import datetime
from elevenlabs import ElevenLabs


load_dotenv()

def generate_valid_news_url(keyword: str) -> str:
    """
    Generate a Google News search URL for a keyword with optional sorting by latest
    
    Args:
        keyword: Search term to use in the news search
        
    Returns:
        str: Constructed Google News search URL
    """
    q = quote_plus(keyword)
    return f"https://news.google.com/search?q={q}&tbs=sbd:1"
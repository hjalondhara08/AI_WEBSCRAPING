import requests
import os
from fastapi import FastAPI, HTTPException
from bs4 import BeautifulSoup
import ollama
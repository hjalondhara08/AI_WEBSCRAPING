from fastapi import FastAPI, HTTPException, File, Response
from fastapi.responses import FileResponse
import os
import uvicorn
from pathlib import Path
from dotenv import load_dotenv

from model import NewsRequest

load_dotenv()   

app = FastAPI()


@app.post("/generate-news-audio")
async def generate_news_audio(request: NewsRequest):
     try:
        results = {}
        
        if request.source_type in ["news", "both"]:
            news_scraper = NewsScraper()
            results["news"] = await news_scraper.scrape_news(request.topics)
        
        if request.source_type in ["reddit", "both"]:
            results["reddit"] = await scrape_reddit_topics(request.topics)

        if age > 15 :
            print("Age is greater than 15")
            
     except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




if __name__ == "__main__":
    
    uvicorn.run(
        "backend:app",
        host="0.0.0.0",
        port=1234,
        reload=True
    )
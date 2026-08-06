from pydantic import BaseModel, Field
from typing import List, Optional

class NewsRequest(BaseModel):
    topics: List[str] = Field(..., description="List of topics to analyze")
    source_type: str = Field(..., description="Type of data source: 'both', 'news', or 'reddit'")
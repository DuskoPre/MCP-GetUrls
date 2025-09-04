from pydantic import BaseModel, Field
from typing import List, Optional

class SearchQuery(BaseModel):
    query: str = Field(..., description="The search query to be used on DuckDuckGo.")

class SearchResult(BaseModel):
    title: str = Field(..., description="The title of the search result.")
    url: str = Field(..., description="The URL of the search result.")
    snippet: Optional[str] = Field(None, description="A snippet of the search result.")

class SearchResults(BaseModel):
    results: List[SearchResult] = Field(..., description="A list of search results.")

class SelectionRequest(BaseModel):
    results: List[SearchResult] = Field(..., description="The list of search results to select from.")
    num_results: int = Field(..., description="The number of results to select.")

class SelectionResponse(BaseModel):
    selected_results: List[SearchResult] = Field(..., description="The selected search results.")
    reasoning: str = Field(..., description="The reasoning behind the selection.")

class FetchParseRequest(BaseModel):
    url: str = Field(..., description="The URL to fetch and parse.")

class FetchParseResponse(BaseModel):
    content: str = Field(..., description="The parsed content of the URL.")

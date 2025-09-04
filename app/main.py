from fastapi import FastAPI, HTTPException
from app.models import SearchQuery, SearchResults, SelectionRequest, SelectionResponse, FetchParseRequest, FetchParseResponse
from app.search import search_web
from app.select import select_best_results
from app.fetch_parse import fetch_and_parse

app = FastAPI(title="MCP-GetUrls", description="A web application to search, select, and fetch-parse content from the web.")

@app.post("/search", response_model=SearchResults)
async def search(query: SearchQuery):
    try:
        results = search_web(query)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/select", response_model=SelectionResponse)
async def select(request: SelectionRequest):
    try:
        response = select_best_results(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/fetch-parse", response_model=FetchParseResponse)
async def fetch_parse(request: FetchParseRequest):
    try:
        response = fetch_and_parse(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

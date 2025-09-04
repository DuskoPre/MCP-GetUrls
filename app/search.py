from duckduckgo_search import ddg
from app.models import SearchQuery, SearchResults, SearchResult
from typing import List

def search_web(query: SearchQuery) -> SearchResults:
    search_results = ddg(query.query, max_results=10)
    results = [
        SearchResult(
            title=result['title'],
            url=result['href'],
            snippet=result['body']
        )
        for result in search_results
    ]
    return SearchResults(results=results)

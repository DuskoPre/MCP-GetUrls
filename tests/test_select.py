from app.models import SelectionRequest, SelectionResponse, SearchResult
from app.select import select_best_results
import pytest

def test_select_best_results():
    results = [
        SearchResult(title="Result 1", snippet="Snippet 1", url="http://example.com/1"),
        SearchResult(title="Result 2", snippet="Snippet 2", url="http://example.com/2"),
        SearchResult(title="Result 3", snippet="Snippet 3", url="http://example.com/3"),
    ]
    request = SelectionRequest(results=results, num_results=2)
    response = select_best_results(request)
    assert isinstance(response, SelectionResponse)
    assert len(response.selected_results) == 2
    assert isinstance(response.reasoning, str)

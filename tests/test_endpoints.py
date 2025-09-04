from fastapi.testclient import TestClient
from app.main import app
from app.models import SearchQuery, SelectionRequest, FetchParseRequest

client = TestClient(app)

def test_search_endpoint():
    query = SearchQuery(query="Python programming")
    response = client.post("/search", json=query.dict())
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "results" in data
    results = data["results"]
    assert isinstance(results, list)
    for result in results:
        assert isinstance(result, dict)
        assert "title" in result
        assert "snippet" in result
        assert "url" in result
        assert isinstance(result["title"], str)
        assert isinstance(result["snippet"], str)
        assert isinstance(result["url"], str)

def test_select_endpoint():
    results = [
        {"title": "Result 1", "snippet": "Snippet 1", "url": "http://example.com/1"},
        {"title": "Result 2", "snippet": "Snippet 2", "url": "http://example.com/2"},
        {"title": "Result 3", "snippet": "Snippet 3", "url": "http://example.com/3"},
    ]
    request = SelectionRequest(results=results, num_results=2)
    response = client.post("/select", json=request.dict())
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "selected_results" in data
    selected_results = data["selected_results"]
    assert isinstance(selected_results, list)
    assert len(selected_results) == 2
    assert "reasoning" in data
    assert isinstance(data["reasoning"], str)

def test_fetch_parse_endpoint():
    request = FetchParseRequest(url="http://example.com/1")
    response = client.post("/fetch-parse", json=request.dict())
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "content" in data
    assert isinstance(data["content"], str)

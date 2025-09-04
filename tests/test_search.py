from fastapi.testclient import TestClient
from app.main import app
from app.models import SearchQuery, SearchResults, SearchResult

client = TestClient(app)

def test_search():
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

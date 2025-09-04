import httpx
from bs4 import BeautifulSoup
from app.models import FetchParseRequest, FetchParseResponse

def fetch_and_parse(request: FetchParseRequest) -> FetchParseResponse:
    try:
        response = httpx.get(request.url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        # Extract text content from the page
        content = soup.get_text(separator='\n', strip=True)
        return FetchParseResponse(content=content)
    except httpx.RequestError as e:
        return FetchParseResponse(content=f"Error fetching the URL: {e}")
    except httpx.HTTPStatusError as e:
        return FetchParseResponse(content=f"HTTP error occurred: {e}")
    except Exception as e:
        return FetchParseResponse(content=f"An unexpected error occurred: {e}")

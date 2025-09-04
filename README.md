# MCP-GetUrls

## Description
MCP-GetUrls is a web application that allows users to search for content on the web, select the best results, and fetch and parse the content of the selected URLs.

## Setup

### Prerequisites
- Python 3.9 or higher
- Poetry (for dependency management)

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/MCP-GetUrls.git
   cd MCP-GetUrls
   ```

2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

3. Activate the virtual environment:
   ```sh
   poetry shell
   ```

## Environment
- **FastAPI**: Web framework for building APIs
- **Pydantic**: Data validation and settings management using Python type annotations
- **Requests**: HTTP library for making requests to web pages
- **BeautifulSoup**: Library for parsing HTML and XML documents

## Usage

### Running the Application
To run the application, use the following command:
```sh
uvicorn app.main:app --reload
```

This will start the FastAPI server with automatic reloading enabled. You can access the application at `http://127.0.0.1:8000`.

### Endpoints
- **POST /search**
  - **Description**: Searches the web for a given query.
  - **Request Body**:
    ```json
    {
      "query": "Python programming"
    }
    ```
  - **Response**:
    ```json
    {
      "results": [
        {
          "title": "Result 1",
          "snippet": "Snippet 1",
          "url": "http://example.com/1"
        },
        ...
      ]
    }
    ```

- **POST /select**
  - **Description**: Selects the best results from a list of search results.
  - **Request Body**:
    ```json
    {
      "results": [
        {
          "title": "Result 1",
          "snippet": "Snippet 1",
          "url": "http://example.com/1"
        },
        ...
      ],
      "num_results": 2
    }
    ```
  - **Response**:
    ```json
    {
      "selected_results": [
        {
          "title": "Result 1",
          "snippet": "Snippet 1",
          "url": "http://example.com/1"
        },
        ...
      ],
      "reasoning": "Reasoning for selection"
    }
    ```

- **POST /fetch-parse**
  - **Description**: Fetches and parses the content of a given URL.
  - **Request Body**:
    ```json
    {
      "url": "http://example.com/1"
    }
    ```
  - **Response**:
    ```json
    {
      "content": "Parsed content of the URL"
    }
    ```

## Testing
To run the tests, use the following command:
```sh
pytest
```

This will execute all the tests in the `tests` directory.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

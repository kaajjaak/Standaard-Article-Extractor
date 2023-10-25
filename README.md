# Standaard Article Extractor

This tool is designed to extract pay-walled articles from the `standaard.be` website. The program utilizes automated user account creation to bypass paywalls and retrieve the full content of the articles. Additionally, it provides a FastAPI server endpoint to fetch articles directly by their IDs.

## Installation:

### Requirements:

- Google Chrome: The web scraper requires Google Chrome to be installed as it uses a Chrome WebDriver.
  
- Python Dependencies: Install the necessary Python packages using the provided `requirements.txt` file.

`pip install -r requirements.txt`


### Project Structure:

- **Main Article Extractor (`main.py`)**:
This script can be executed from the command line to extract articles. It supports both direct output to a file and piping to the console.

- **FastAPI Server (`main_api.py`)**:
Provides an API interface to retrieve articles. When running, articles can be fetched via the endpoint `localhost:8000/cnt/{article_id}`.

## Usage:

### Command Line Article Extraction:

Navigate to the project directory and run:

`python main.py <URL_OF_THE_ARTICLE> [--pipe]`

Arguments:

- `URL_OF_THE_ARTICLE`: The direct URL of the article you want to extract from `standaard.be`.
  
- `--pipe`: (Optional) Use this flag if you want the article content to be printed to the console instead of being saved to `article.html`.

### Using the FastAPI Server:

Start the FastAPI server using:

`uvicorn main_api:app --reload`

Once the server is running, you can access articles by navigating to:

`http://localhost:8000/cnt/{article_id}`


Replace `{article_id}` with the ID of the article you wish to retrieve.

## Notes:

- Make sure Google Chrome is installed on your system as the application relies on it for web scraping.
  
- For the application to work efficiently and remain undetectable, it's recommended to run it occasionally and not bombard the `standaard.be` website with numerous rapid requests.

## Contributing:

If you have suggestions for improving this tool, please open an issue or submit a pull request. All contributions are welcome!

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

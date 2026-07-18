# News Article Summariser

📰 A Streamlit web application that generates concise and structured summaries of news articles from their URLs.

Simply paste a news article link, choose a summary length, and receive an easy-to-read summary along with key points, estimated reading time, and the original article text for reference.

---

## Features

* Summarise news articles directly from URLs
* Choose between **Short**, **Medium**, and **Detailed** summaries
* Extract key points from articles
* Display estimated reading time
* View original article content alongside the summary
* Fast and responsive Streamlit interface
* Supports manual text input when article extraction fails

---

## Demo

1. Open the application in your browser.
2. Paste a news article URL.
3. Select your preferred summary length.
4. Click **Summarize**.
5. View the generated summary and key insights.

Add screenshots or a GIF below:

```markdown
![Screenshot](docs/screenshot.png)
```

```markdown
![Demo](docs/demo.gif)
```

---

## Tech Stack

* Python
* Streamlit
* Requests
* BeautifulSoup4
* Newspaper3k
* Transformers (optional)
* PyTorch (optional)

---

## Requirements

* Python 3.8+
* Streamlit
* Required libraries listed in `requirements.txt`

Example:

```txt
streamlit
requests
beautifulsoup4
newspaper3k
transformers
torch
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Kartikesh001/News-article-summariser.git
cd News-article-summariser
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install the essentials manually:

```bash
pip install streamlit newspaper3k beautifulsoup4 requests
```

---

## Running the Application

🚀 Start the Streamlit server:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

If your entry file has a different name, replace `app.py` accordingly.

---

## Usage

1. Paste a valid news article URL.
2. Select a summary length.
3. Click **Summarize**.
4. The application will:

   * Extract article content
   * Generate a summary
   * Highlight key points
   * Estimate reading time
   * Display the original article text

If article extraction fails, manually paste the article text (if supported).

---

## Configuration

If using an external API, store your API key as an environment variable.

**Linux / macOS**

```bash
export OPENAI_API_KEY="your_api_key_here"
```

**Windows PowerShell**

```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

Access it in Python:

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

---

## Troubleshooting

### Article Extraction Fails

* Some websites block web scrapers.
* Certain sites load content dynamically using JavaScript.
* Try another article or use manual text input.

### Slow Summary Generation

* Large transformer models can be resource-intensive.
* Consider using a smaller model or an API-based solution.

---

⭐ If you found this project useful, consider giving it a star.

import streamlit as st
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import os

# Set up the Google API key from Streamlit secrets
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except KeyError:
    st.error("API Key not found. Please set `GOOGLE_API_KEY` in `secrets.toml`.")
    st.stop()

# Function to scrape article content from a URL
def scrape_article(url):
    """
    Scrapes the text content from a given news article URL.
    Returns the scraped text or an error message.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        # Fetch the content of the URL
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the main body of the text. This is a common pattern for news articles.
        # This part might need to be adjusted for different websites.
        paragraphs = soup.find_all('p')
        article_text = ' '.join([p.get_text() for p in paragraphs])
        
        if not article_text:
            return "Error: Could not extract article text. The website's structure may be too complex."
            
        return article_text

    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"

# Function to analyze the article using the Gemini API
def analyze_article(text):
    """
    Sends the article text to the Gemini API for critical analysis.
    Returns the analysis report in Markdown format.
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Craft a detailed prompt for the AI to follow
    prompt = f"""
    You are an AI designed to act as a "Digital Skeptic." Your task is to provide a critical analysis of a news article.

    Analyze the following article content and create a detailed report in Markdown format. The report should have three main sections with clear headings:

    ## 1. Core Claims
    - List 3-5 of the main facts, arguments, or central claims presented in the article.
    - Be concise and objective. Use bullet points for readability.

    ## 2. Language & Tone Analysis
    - Describe the overall tone of the article (e.g., neutral, biased, sensational, alarmist, informative).
    - Analyze the language used. Point out any emotionally charged words, loaded language, or rhetorical devices.
    - Give specific examples from the text to support your analysis.

    ## 3. Potential Red Flags
    - Identify any potential issues that a critical reader should be aware of.
    - Examples of red flags include:
        - Missing or vague sources (e.g., "experts say" without attribution).
        - Lack of counter-arguments or a one-sided perspective.
        - Clickbait-style headlines or sensationalism.
        - Inconsistent or contradictory information.
        - Obvious logical fallacies.

    Article Content:
    ---
    {text[:5000]}  # Limit text to avoid token limits.
    ---
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating analysis: {e}"

# --- Streamlit UI and Application Logic ---

st.set_page_config(page_title="The Digital Skeptic AI", layout="wide")

st.title("🕵️ The Digital Skeptic AI")
st.markdown("---")

st.subheader("Empowering Critical Thinking in an Age of Information Overload")
st.write("Enter a URL of a news article below to receive a critical analysis report.")

# Use a container for better spacing and organization
with st.container():
    url = st.text_input("Enter a news article URL:", key="url_input")

    # Use columns to center the button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Analyze Article", use_container_width=True):
            if url:
                with st.spinner("Analyzing article... This may take a moment."):
                    # Step 1: Scrape the article content
                    article_content = scrape_article(url)

                    if article_content.startswith("Error"):
                        st.error(article_content)
                    else:
                        # Step 2: Get the analysis from the AI
                        analysis_report = analyze_article(article_content)
                        
                        # Step 3: Display the report in Markdown
                        st.subheader("Critical Analysis Report")
                        st.markdown(analysis_report)
                        st.success("Analysis complete!")
                        
                        # Step 4: Add a download button for the report
                        st.download_button(
                            label="Download Report as Markdown",
                            data=analysis_report,
                            file_name="news_analysis_report.md",
                            mime="text/markdown"
                        )
            else:
                st.warning("Please enter a valid URL.")

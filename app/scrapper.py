"""
Basic Scraping using BeautifulSoup.
"""
import requests
from bs4 import BeautifulSoup

def fetch_hospital_info(url: str) -> dict:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return {"url": url, "error": str(e)}

    soup = BeautifulSoup(response.text, "html.parser")
    departments = [d.get_text(strip=True) for d in soup.select(".department")]
    return {"url": url, "departments": departments}

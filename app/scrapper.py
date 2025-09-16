import requests
from bs4 import BeautifulSoup

def fetch_hospital_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Parse data, e.g., list of departments
    departments = [d.text for d in soup.select(".department")]
    return {"url": url, "departments": departments}

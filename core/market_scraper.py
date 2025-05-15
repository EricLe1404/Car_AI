import requests
from bs4 import BeautifulSoup

def scrape_carsales(make, model):
    search_url = f"https://www.carsales.com.au/cars/{make}/{model}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(search_url, headers=headers)
        if response.status_code != 200:
            return f"Failed to fetch data. Status code: {response.status_code}"
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Example: Find prices (You’ll need to adjust this based on the actual HTML structure)
        prices = []
        for price_tag in soup.find_all("span", class_="price"):  
            price_text = price_tag.get_text(strip=True).replace("$", "").replace(",", "")
            if price_text.isdigit():
                prices.append(int(price_text))

        return prices if prices else "No prices found."

    except Exception as e:
        return f"Error: {e}"

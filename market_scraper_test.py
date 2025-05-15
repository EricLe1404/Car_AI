import requests
from bs4 import BeautifulSoup

def scrape_carsales(make, model):
    search_url = f"https://www.carsales.com.au/cars/{make}/{model}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Connection": "keep-alive",
}

    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        if response.status_code != 200:
            return f"❌ Failed to fetch data. Status code: {response.status_code}"
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        prices = []
        for price_tag in soup.find_all("span", class_="Price__Amount-sc-1l5f7v6-0"):
            price_text = price_tag.get_text(strip=True).replace("$", "").replace(",", "")
            if price_text.isdigit():
                prices.append(int(price_text))

        return prices if prices else "❌ No prices found."

    except Exception as e:
        return f"❌ Error occurred: {e}"

# 🎯 Test the Scraper Here
if __name__ == "__main__":
    make = "lexus"
    model = "is350"
    prices = scrape_carsales(make, model)
    print(f"💰 Prices found for {make.title()} {model.upper()}: {prices}")

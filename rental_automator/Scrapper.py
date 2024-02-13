import requests
from bs4 import BeautifulSoup
RENTAL_SEARCH_URL = "https://appbrewery.github.io/Zillow-Clone/"


class Scrapper:

    def __init__(self):
        self.soup = BeautifulSoup(requests.get(RENTAL_SEARCH_URL).text,
                                  "html.parser")
        self.links_to_properties = self.generate_links()
        self.price_per_month = self.generate_prices()
        self.addresses = self.generate_addresses()

    def clear_price_text(self, price):
        return price.replace("+", "-").replace("/", "-").split("-")[0]

    def clear_address(self, address):
        clean_address = address.strip().split(" | ")
        if len(clean_address) > 1:
            return clean_address[1]
        else:
            return clean_address[0]

    def generate_links(self):
        photo_properties = self.soup.select(".StyledPropertyCardPhotoBody a")
        return [tag.get("href") for tag in photo_properties]

    def generate_prices(self):
        price_properties = self.soup.select(".PropertyCardWrapper span")
        return [self.clear_price_text(tag.text) for tag in price_properties]

    def generate_addresses(self):
        estate_addresses = self.soup.select(".StyledPropertyCardDataWrapper a address")
        return [self.clear_address(tag.text) for tag in estate_addresses]
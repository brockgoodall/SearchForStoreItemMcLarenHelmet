# Import libraries/modules
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import http.client
import urllib

# Read URL
page_url = "https://www.mclarenstore.com/en/search/?pmin=0%2C00&q=helmet&start=0&sz=100" # Showing 100 items
req = Request(page_url , headers={'User-Agent': 'Mozilla/5.0'})
page_html = urlopen(req).read()
page_soup = soup(page_html, "html.parser")

# Parse URL for the details I need
searchResults = page_soup.findAll("div",{"class":"product"})
for searchResult in searchResults:
    title = searchResult.find("a",{"class":"product-tile-body-link"}).text
    price = searchResult.find("div",{"class":"price"}).text.strip()
    url = searchResult.a["href"]
    formattedURL = "https://www.mclarenstore.com" + url
    if "Lando" in title:
        print("Lando helmet found!")
        print(title)
        print(price)
        print("mclarenstore.com" + url)
        print("\n")
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
                     urllib.parse.urlencode({
                         "token": "YOUR API KEY HERE",
                         "user": "YOUR USER KEY HERE",
                         "title": "Lando Helmet Found",
                         "message": title + " " + price,
                         "url": formattedURL,
                     }), {"Content-type": "application/x-www-form-urlencoded"})
        conn.getresponse()
    else:
        if "lando" in title:
            print("Lando helmet found!")
            print(title)
            print(price)
            print("mclarenstore.com" + url)
            print("\n")
            conn = http.client.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
                         urllib.parse.urlencode({
                             "token": "YOUR API KEY HERE",
                             "user": "YOUR USER KEY HERE",
                             "title": "Lando Helmet Found",
                             "message": title + " " + price,
                             "url": formattedURL,
                         }), {"Content-type": "application/x-www-form-urlencoded"})
            conn.getresponse()
        else:
            print("No Lando helmet found.")

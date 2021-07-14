import requests
import csv
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/psycho-sanitarium-psycho-15_628/index.html'
response = requests.get(url)

def saveBooksInfos():

    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')

        # extract all informations and remove html tags with .text
        product_page_url = url
        information = soup.find('table', attrs={'class': 'table-striped'})
        universal_product_code = information.find_all('td')[0].text
        title = soup.find('h1').text
        price_including_tax = information.find_all('td')[3].text[1:]
        price_excluding_tax = information.find_all('td')[2].text[1:]
        number_available = information.find_all('td')[5].text
        product_description = soup.find_all('p')[3].text
        category = soup.find_all('li')[2].text[1:]
        review_rating = information.find_all('td')[6].text
        image_src = soup.find("div", {"class": "item active"}).find("img")
        image_url = image_src["src"]

    with open("P2_01_codesource.csv", "w", encoding="utf8", newline='') as outf:
        write = csv.writer(outf)
        header = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax',
                'number_available', 'product_description', 'category', 'review_rating', 'image_url\n']
        info = [product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
                number_available, product_description, category, review_rating, image_url]

        # write header first and then info into our file
        write.writerow(header)
        write.writerow(info)
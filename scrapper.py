import requests
import csv
from bs4 import BeautifulSoup

def saveBook(url_book):
    response = requests.get(url_book)

    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')

        # extract all informations and remove html tags with .text
        product_page_url = url_book
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

    # save info in a csv file
    with open("P2_01_codesource.csv", "a", encoding="utf8", newline='') as outf:
        write = csv.writer(outf)
        info = [product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
                number_available, product_description, category, review_rating, image_url]

        # write info into our file
        write.writerow(info)

# get all book from the category
def get_all_book_from_cat(url_cat):
    url_cat_page = url_cat + 'index.html'

    # save info in a csv file
    with open("P2_01_codesource.csv", "w", encoding="utf8", newline='') as outf:
        write = csv.writer(outf)
        header = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax',
                'number_available', 'product_description', 'category', 'review_rating', 'image_url\n']
        # write header
        write.writerow(header)

    # loop in all page
    while True:
        response = requests.get(url_cat_page)
        soup = BeautifulSoup(response.text, 'lxml')

        # loop to get all the book url in the category
        for books in soup.find_all('div', {'class': 'image_container'}):
            url_book = books.find('a', href= True)
            url_book = url_book['href'].split('..')[3]
            url_book = 'https://books.toscrape.com/catalogue' + url_book
            saveBook(url_book)

        # retrieve next page url
        next_page = soup.find_all('li', {'class': 'next'})
        if len(next_page) != 0:
            url_page = next_page[0].find('a', href= True)
            url_page = url_page['href']
            url_cat_page = url_cat + url_page
            print(url_cat_page)
        else:
            break

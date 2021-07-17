import requests
import csv
import os
from bs4 import BeautifulSoup

folder_csv =  'csv'
if not os.path.exists(folder_csv):
    os.makedirs(folder_csv)

def saveBook(url_book, category_name):
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
        review_rating = soup.find('p', class_='star-rating').get('class')[1]
        image_src = soup.find("div", {"class": "item active"}).find("img")
        image_url = image_src["src"]

    # save info in a csv file
    with open(folder_csv + '/' + category_name + '.csv', 'a', encoding='utf8', newline='') as outf:
        write = csv.writer(outf)
        info = [product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
                number_available, product_description, category, review_rating, image_url]

        # write info into our file
        write.writerow(info)

# get all book from the category
def get_all_book_from_cat(url_cat, category_name):
    url_cat_page = url_cat

    # save info in a csv file
    with open(folder_csv + '/' + category_name + '.csv', "w", encoding="utf8", newline='') as outf:
        write = csv.writer(outf)
        header = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax',
                'number_available', 'product_description', 'category', 'review_rating', 'image_url\n']
        # write header
        write.writerow(header)

    print('retrieving all books from cat ' + url_cat_page)

    # loop in all page
    while True:
        response = requests.get(url_cat_page)
        soup = BeautifulSoup(response.text, 'lxml')

        # loop to get all the book url in the category
        for books in soup.find_all('div', {'class': 'image_container'}):
            url_book = books.find('a', href= True)
            url_book = url_book['href'].split('..')[3]
            url_book = 'https://books.toscrape.com/catalogue' + url_book
            saveBook(url_book, category_name)

        # retrieve next page url
        next_page = soup.find_all('li', {'class': 'next'})
        if len(next_page) != 0:
            url_page = next_page[0].find('a', href= True)
            url_page = url_page['href']
            url_cat_page = url_cat + url_page
        else:
            break

def get_all_category(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    # loop to get all category name
    categories = soup.find('ul', class_='nav nav-list').li.ul.find_all('li')
    for category in categories:
        link = category.find('a')['href']
        category_name = category.find('a').text.strip()
        get_all_book_from_cat(url + link, category_name)

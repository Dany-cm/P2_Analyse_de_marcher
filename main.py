from scrapper import get_book_url, saveBooks

url = 'https://books.toscrape.com/catalogue/category/books/horror_31/index.html'

if __name__ == "__main__":
    get_book_url(url, write='P2_01_codesource.csv')
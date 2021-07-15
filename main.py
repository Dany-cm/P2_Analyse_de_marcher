from scrapper import get_all_book_from_cat

url = 'https://books.toscrape.com/catalogue/category/books/horror_31/'

if __name__ == "__main__":
    get_all_book_from_cat(url)
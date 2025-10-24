from requests import get
from pprint import PrettyPrinter

Base_URL = "https://openlibrary.org"    #defines base part of api data
ALL_JSON = "/search.json?q=python"   #defines the end point upto which the data is returned
printer = PrettyPrinter()
docs = get(Base_URL + ALL_JSON).json()['docs'] #combines to form the full URL and sends get request to fetch data

for doc in docs:
    book_author = doc.get('author_name')
    book_title = doc['title']
    year = doc.get('first_publish_year')
   
    print(f"{book_title} by {book_author}, {year}")
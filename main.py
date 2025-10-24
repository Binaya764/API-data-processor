from requests import get
from pprint import PrettyPrinter

Base_URL = "https://openlibrary.org"    #defines base part of api data
ALL_JSON = "/search.json?q=python"   #defines the end point upto which the data is returned
printer = PrettyPrinter()

def books_data():
    docs = get(Base_URL + ALL_JSON).json()['docs'] #combines to form the full URL and sends get request to fetch data


    docs.sort(key=lambda x: x.get('title',0))   #sorting by title .get to handle if the title is missing
    for i, doc in enumerate(docs):

        book_author = doc.get('author_name')
        book_title = doc['title']
        year = doc.get('first_publish_year')
        book_language = doc.get('language')
        print("")
        print(f"{i+1}. {book_title} by {book_author}, {year},{book_language}")
        
books_data()
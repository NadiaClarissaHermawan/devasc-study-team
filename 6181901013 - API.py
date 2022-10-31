# Nadia Clarissa Hermawan / 6181901013

#!/usr/bin/env python3

import requests
import json
from faker import Faker


APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

#get token
def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")

#add books
def addBook(book, apiKey):
    r = requests.post(
        f"{APIHOST}/api/v1/books", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            },
        data = json.dumps(book)
    )
    if r.status_code == 200:
        print(f"Book {book} added.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to add book {book}.")

#list books
def listBooks(includeISBN="false", sortBy="", author="", page=0):
    str1 = APIHOST + "/api/v1/books?includeISBN=" + includeISBN + "&page=" + str(page)
    if sortBy != "":
        str1 = str1 + "&sortBy=" + sortBy

    if author != "":
        str1 = str1 + "&author=" + author

    r = requests.get(
        f"{str1}"
    )
    if r.status_code == 200:
        print(r.json())
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to get books list.")
        

#list specific book
def listSpecificBooks(id):
    r = requests.get(
        f"{APIHOST}/api/v1/books/{id}",
    )
    if r.status_code == 200:
        print(r.json())
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to get specific books list.")


#delete book
def deleteBook(id):
    r = requests.delete(
        f"{APIHOST}/api/v1/books/{id}",
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            }
    )
    if r.status_code == 200:
        print(r.json())
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to delete specific book.")



# Get the Auth Token Key
apiKey = getAuthToken()

# Using the faker module, generate random "fake" books
fake = Faker()
for i in range(6, 106):
    fakeTitle = fake.catch_phrase()
    fakeAuthor = fake.name()
    fakeISBN = fake.isbn13()
    book = {"id":i, "title": fakeTitle, "author": fakeAuthor, "isbn": fakeISBN}
    # add book
    addBook(book, apiKey) 

#get books list
listBooks("true", "author")

#get specific books list
listSpecificBooks(2)

#delete specific book
deleteBook(1)

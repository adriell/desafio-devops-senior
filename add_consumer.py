from pprint import pprint

import requests


def main():
   
    book = requests.post('http://localhost:8001/services/book-manager/plugins', data={
        "name": "key-auth"
    })
    desafio = requests.post('http://localhost:8001/routes/desafio/plugins', data={
        "name": "key-auth"
    })  


if __name__ == '__main__':
    main()
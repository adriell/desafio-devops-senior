from pprint import pprint

import requests


def main():
    response = requests.post('http://localhost:8001/services/', data={
        "name": "book_manager",
        "url": "http://book_manager:5000"
    })
    pprint(response.json())


if __name__ == '__main__':
    main()
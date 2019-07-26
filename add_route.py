from pprint import pprint

import requests


def main():
    response = requests.post('http://localhost:8001/services/book/routes', data={
        "paths": '/desafio'
    })
    pprint(response.json())

    add = requests.post('http://localhost:8001/services/book/routes', data={
        "paths": '/add'
    })
    pprint(add.json())

    update = requests.post('http://localhost:8001/services/book/routes', data={
        "paths": '/update'
    })
    pprint(update.json())

    delete = requests.post('http://localhost:8001/services/book/routes', data={
        "paths": '/delete'
    })
    pprint(delete.json())


if __name__ == '__main__':
    main()
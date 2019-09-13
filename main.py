import requests

if __name__ == '__main__':
    url = 'http://www.omdbapi.com/'
    response = requests.get(url)

    if response.status_code == 200:
        print(response.content)
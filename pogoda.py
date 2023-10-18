import requests

URL = 'http://wttr.in'

def get_weather(city: str, lang: str = 'ru') -> None:
    url_city = '{0}/{1}'.format(URL, city)
    params = {
        'nTqM': '',
        'lang': lang
    }
    response = requests.get(url_city, params=params)
    try:
        if not response.raise_for_status():
            return response.text
    except:
        return None


def main(city: str) -> None:
    result = get_weather(city)
    if not result:
        print('Ошибка запроса')
    else:
        print(result)


if __name__ == '__main__':
    main('moscow')

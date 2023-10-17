import requests

URL = 'http://wttr.in'


class Weather:
    def __init__(self, city: str, lang: str = 'en') -> None:
        self.city = city
        self.lang = lang

    def change_lang(self, lang: str) -> None:
        self.lang = lang

    def change_city(self, city: str) -> None:
        self.city = city

    def get_weather(self) -> None:
        url_city = URL + '/' + self.city
        params = {
            'nTqM': '',
            'lang': self.lang
        }
        response = requests.get(url_city, params=params)
        if not response.raise_for_status():
            print(response.url, response.text, sep='\n')
        else:
            print(response.status_code)
    

def get_weather(city: str, lang: str = 'ru') -> None:
    url_city = URL + '/' + city
    url_city = '{0}/{1}'.format(URL, city)
    params = {
        'nTqM': '',
        'lang': lang
    }
    response = requests.get(url_city, params=params)
    if not response.raise_for_status():
        print(response.url, response.text, sep='\n')
    else:
        print(response.status_code)


get_weather('лондон', 'ru')

weather_object = Weather('london')
weather_object.get_weather()
weather_object.change_city('москва')
weather_object.change_lang('ru')
weather_object.get_weather()

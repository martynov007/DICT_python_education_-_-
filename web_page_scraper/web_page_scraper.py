import json
from pydoc import describe
import requests as req
from bs4 import BeautifulSoup as bs


class WebPageScraper:
    
    def __init__(self) -> None:
        headers = {'Accept-Language': 'en-US,en;q=0.5'}
        url = input('Enter your url:')

        res = req.get(url, headers=headers)
        
        if not res:
            print('Invalid resource!')
            return

        soup = bs(res.text, 'html.parser')

        title_html = soup.find('title')
        script_dict = json.loads(soup.find('script', type='application/ld+json').string)
        
        if not title_html or not script_dict:
            print('Invalid resource!')
            return

        self.show_film_dict(title_html.text, script_dict.get('description'))

    @staticmethod
    def show_film_dict(title, description):
        film_dict = {
            'title': title,
            'description': description
        }

        print(film_dict)


if __name__ == "__main__":
    WebPageScraper()
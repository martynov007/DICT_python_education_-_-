import requests as req
import os

class WebPageScraper:
    
    def __init__(self) -> None:
        headers = {'Accept-Language': 'en-US,en;q=0.5'}
        url = input('Enter your url:')

        res = req.get(url, headers=headers)
        
        if not res:
            print('The URL returned {}'.format(res.status_code))
            return

        pg_html_content = res.content

        with open(os.path.join('web_page_scraper','source.html'), mode='wb') as f:
            f.write(pg_html_content)
            print('Content saved!')

if __name__ == "__main__":
    WebPageScraper()
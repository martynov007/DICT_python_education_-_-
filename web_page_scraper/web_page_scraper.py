import string
import requests as req
import os
from bs4 import BeautifulSoup as bs


class WebPageScraper:
    
    def __init__(self) -> None:
        headers = {'Accept-Language': 'en-US,en;q=0.5'}
        url = input('Enter your url:')
        base_url = 'https://www.nature.com'
        res = req.get(url, headers=headers)
        
        if not res:
            print('The URL returned {}'.format(res.status_code))
            return

        soup = bs(res.text, 'html.parser')

        data_tests = soup.find_all('span', {'data-test':'article.type'})
        data_track_actions = soup.find_all('a', {'data-track-action': "view article"})
        
        saved_articles = []

        for dt, dta in zip(data_tests,data_track_actions):
            article = dt.get_text().strip('\n').lower()

            if article != 'news':
                continue

            article_res = req.get(base_url + dta['href'], headers=headers)

            if not article_res:
                print('Invalid resource!Cant get body and title for this article')
                continue
            
            soup2 = bs(article_res.text, 'html.parser')
            translator = str.maketrans('','',string.punctuation)
            prep_title = str.translate(soup2.title.text, translator)
            prep_title = prep_title.replace(' ', '_')

            with open(os.path.join('web_page_scraper',f'{prep_title}.html'), mode='wb') as f:
                article_body = soup2.body
                wrapped_artl_body = article_body.wrap(soup2.new_tag("div"))
                encoded_body = wrapped_artl_body.encode('utf-8')

                f.write(encoded_body)
                saved_articles.append(prep_title)

        print('Saved articles: ', saved_articles)

if __name__ == "__main__":
    WebPageScraper()
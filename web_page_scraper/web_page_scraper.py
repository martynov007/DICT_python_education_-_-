from genericpath import exists
import string
import requests as req
import os
from bs4 import BeautifulSoup as bs
import urllib.parse 

class WebPageScraper:
    
    def __init__(self) -> None:
        headers = {'Accept-Language': 'en-US,en;q=0.5'}
        pages_count = int(input('Enter pages count:'))
        article_type = input('Enter article type:')
        base_url = 'https://www.nature.com'
        articles_url = urllib.parse.urljoin(base_url, 'nature/articles')
        params = {
                'sort': 'PubDate',
                'year': 2022,
                'page': 0,
            }

        for pg_nmbr in range(1, pages_count+1):
            try:
                os.mkdir(f'./web_page_scraper/Page_{pg_nmbr}')
            except OSError:
                pass
            
            params['page'] = pg_nmbr
            res = req.get(articles_url, headers=headers, params=params)

            soup = bs(res.text, 'html.parser')

            data_tests = soup.find_all('span', {'data-test':'article.type'})
            data_track_actions = soup.find_all('a', {'data-track-action': "view article"})
            
            saved_articles = []

            for dt, dta in zip(data_tests,data_track_actions):
                article = dt.get_text().strip('\n').lower()

                if article != article_type.lower():
                    continue

                article_res = req.get(base_url + dta['href'], headers=headers)

                if not article_res:
                    print('Invalid resource!Cant get body and title for this article')
                    continue
                
                soup2 = bs(article_res.text, 'html.parser')
                translator = str.maketrans('','',string.punctuation)
                prep_title = str.translate(soup2.title.text, translator)
                prep_title = prep_title.replace(' ', '_')

                with open(os.path.join('web_page_scraper',f'Page_{pg_nmbr}',f'{prep_title}.html'), mode='wb', ) as f:
                    article_body = soup2.body.find_all('p')
                    all_text = ''.join([x.text for x in article_body])
                    new_tag = soup2.new_tag("div")
                    new_tag.string = all_text

                    encoded_body = new_tag.encode('utf-8')

                    f.write(encoded_body)
                    saved_articles.append(prep_title)

        print('Saved all articles')

if __name__ == "__main__":
    WebPageScraper()
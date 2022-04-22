import requests as req

class WebPageScraper:
    def __init__(self) -> None:
        url = input('Enter your url:')
        res = req.get(url)

        if not res:
            print('Invalid resource!')
            return
        
        if not res_js.get('content'):
            print('Resource dont have a quote!')
            return

        res_js = res.json()
        print(res_js['content'])

if __name__ == "__main__":
    WebPageScraper()
import requests
import logging
import sys
from bs4 import BeautifulSoup


def AzureDevOpsScraper():
    URL = 'https://devblogs.microsoft.com/devops/'

    try:
        devopsblog = requests.get(URL)
        parse = BeautifulSoup(devopsblog.text, "html.parser")

        print('Pulling data from...')
        print(parse.title)

        dList = []
        for i in parse.find_all('a'):
            urlParse = i.attrs["href"]
            if urlParse.startswith(URL + 'devops/') \
                and not urlParse.endswith('-rtw/') \
                    and not urlParse.startswith(URL + 'author/') \
                    and not urlParse.startswith(URL + 'page/'):
                dList.append(urlParse)
                print(urlParse)
                if len(dList) > 9:
                    sys.exit(0)

    except Exception as e:
        logging.error(msg='Please see error below')
        print(e)

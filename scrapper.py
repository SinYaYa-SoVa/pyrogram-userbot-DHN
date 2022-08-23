import requests
import urllib.request
import logging
from bs4 import BeautifulSoup


def scrapper():
    url = 'https://www.calend.ru/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        holiday_text = soup.find('div', class_='caption')
        holiday_image = soup.find('div', class_='image')

        if isinstance(holiday_text, type(None)):
            raise NameError('NoneTag')

        txt = str(holiday_text.text).split(':')
        txt = txt[1]
        txt = str(txt).split(',')
        txt = txt[0]

        img = str(holiday_image).split('\'')
        img = img[1]

        urllib.request.urlretrieve(img, "picture.jpg")

        print('Tags successfully fetched!')
        return txt, img
    except NameError:
        logging.error('Something\'s wrong with fetching tags! None variables are found!')


if __name__ == '__main__':
    text, image = scrapper()
    print('The holiday is: {}\nThe picture\'s url is: {}'.format(text, image))

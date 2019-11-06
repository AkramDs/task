import requests
import lxml
import csv
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('lalafo.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['title'],
                         data['price'],
                         data['location'],
                         data['url'],
                         data['photo']))


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    total_pages = soup.find('div', id='listing').find('ul', class_='pagn').find('li', class_='pagn-last').find('a').get('data-page')

    return int(total_pages)

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find('div', id='main-listing-block').find_all('article', class_='listing-item ')

    for ad in ads:
        try:
            title = ad.find('a', class_='item listing-item-title').text.strip()
        except:
            title = ''

        try:
            price = ad.find('p', class_='listing-item-title').text.strip().strip('\xa0KGS')
        except:
            price = ''

        try:
            l = ad.find('div', class_='listing-item-meta').find('span', class_='mr-2').text.strip()
            l2 = ad.find('div', class_='listing-item-meta').find_all('span')[-1].text

            location = l + ' ' + l2
        except:
            location = ''

        try:
            url = 'https://lalafo.kg' + ad.find('div', class_='listing-item-main').find('a', class_='item listing-item-title').get('href')

        except:
            url = ''

        try:
            photo = ad.find('div', class_='swiper-slide swiper-slide-active').find('img', class_='listing-item-photo link-image').get('src')
        except:
            photo = ''

        data = {'title': title,
                'price': price,
                'location': location,
                'url': url,
                'photo': photo}

        write_csv(data)

def main():
    url = 'https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary/mobilnye-telefony?page='

    #total_pages = get_total_pages(get_html(url))

    for i in range(1, 2):#total_pages):
        url_gen = url + str(i)

        get_page_data(get_html(url_gen))


if __name__ == '__main__':
    main()

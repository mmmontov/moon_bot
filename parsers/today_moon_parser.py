from bs4 import BeautifulSoup
import requests

main_url = 'https://phasesmoon.com/russia/primorsky-krai/'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

def get_today_moon():
    today_moon_data = {} 

    req = requests.get(url=main_url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')

    today_date = soup.find(class_='todayprayer row').find(class_='col6').find('h2').text
    moon_data = soup.find(class_='todayprayer row').find(class_='col6').find('tbody').find_all('tr')

    for property, value in map(lambda x: x.text.strip().split('\n'), moon_data):
        today_moon_data[property] = value
    
    return today_date, today_moon_data

def get_today_moon_pic():
    req = requests.get(url=main_url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')

    moon_pic_link = soup.find('body').find(class_='headerdetails').find('img')
    return moon_pic_link['src']


# print(get_today_moon())
print('парсер подключен')
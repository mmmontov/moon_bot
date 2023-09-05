from bs4 import BeautifulSoup
import requests

main_url = 'https://phasesmoon.com/russia/primorsky-krai/'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

def get_week_moons():
    week_moons_data = {}

    req = requests.get(url=main_url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')

    table_head = soup.find('body').find(class_='min-500').find('thead').find('tr')
    table_lines = soup.find('body').find(class_='min-500').find('tbody').find_all('tr')
    
    week_table = []

    head = [i for i in table_head.text.strip().split('\n') if i != ''][1:]

    for line in table_lines:
        date, *other = [i for i in line.text.strip().split('\n') if i != '']
        date = date
        other = [f'{k}: {v}' for k, v in zip(head, other)]
        week_table.append((date, other))
    return week_table



# print(get_week_moons())
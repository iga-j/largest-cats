from bs4 import BeautifulSoup
from googlesearch import search
import requests

def header(title, permalink):
    return '---\nlayout: page\ntitle: ' + title + '\npermalink: ' + permalink + '\n---\n'

def load():
    link = 'https://cats.com/large-cat-breeds'
    response = requests.get(link)

    page = BeautifulSoup(response.text, 'html.parser')

    lista = page.find_all('div', class_='su-row card-review')
    baseurl = 'https://iga-j.github.io/largest-cats/'

    with open('ranking.md', 'w') as f:
        f.write(header('Top 10 Largest Cat Breeds - Ranking', '/ranking'))

        for div in lista:
            f.write('## ' + div.find('h2').text + '\n')
            breed = str(div.find('h2').text)[3:].strip()
            with open(breed.replace(' ', '-') + '.md', 'w') as f2:
                f2.write(header(breed, '/' + breed.replace(' ', '-')))

                f2.write('# **' + breed + '** - more information \n')
                for url in search(breed, stop=3):
                    f2.write('- [' + url + '](' + url + ') \n')
            for item in div.find_all('div', class_='table-item'):
                title = item.find('span', class_='table-item-title').text
                f.write('- ' + str(title).split(':')[0].strip() + ': ' + item.find('span', class_='table-item-value').text  + '\n')
            f.write('- [Find out more](' + baseurl + breed.replace(' ', '-') + ') \n')


if __name__=='__main__':
    load()

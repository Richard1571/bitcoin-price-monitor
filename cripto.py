import banner
import requests
from bs4 import BeautifulSoup

class Coin(object):

    def __init__(self):
        self.url = "https://coinmarketcap.com/"
        self.site = requests.get(self.url)
        self.text = BeautifulSoup(self.site.text, "html.parser")

    def imprim_banner(self):
        self.banner_cripto = banner.banner_text
        print('\033[32m'+self.banner_cripto+'\033[32m')

        self.text_user = 'Desenvolvido por : Richard'
        self.text_git = 'Github : https://github.com/Richard1571'
        print(self.text_user.center(50, ' '))
        print(self.text_git.center(50, ' '))
        print('\033[0;0m')

    def search_element(self):
        self.moeda = self.text.find_all('a', {'class':'currency-name-container'})
        self.price = self.text.find_all('a', {'class':'price'})

        for box in range(10):
            ajusta = 44 - len(self.moeda[box].text) + len(self.price[box].text)
            print('\033[33m'+self.moeda[box].text+'\033[33m', end='')
            print('\033[33m'+self.price[box].text.rjust(ajusta, ' ')+'\033[33m')

teste = Coin()
teste.imprim_banner()
teste.search_element()

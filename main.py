import sys
import requests
import bs4
from random import randint
import re

print("Fang Lazy Crawler ver: 0.01")
server = input("Enter the server you want to scrape from (eune/euw/na): ")
summoner_url = input("Enter the starting summoner name: ")
how_much = int(input("How many sites do you want to scrape (1 site ~~ 110 nicks, 1,5k combos): "))
root_url = 'http://'+ server +'.op.gg/summoner/userName='
nick_arr = []
used_nicks = []
endings = ['pl', 'cz', 'srb', 'gr', 'sk', 'xd']

def rchop(thestring, endings):
    for end in endings:
      if thestring.endswith(end):
        return thestring[:-len(end)]
    else:
      return thestring

def clean_my_shit(nickarr, endings):
    for (index, nick) in enumerate(nick_arr):
         nick_arr[index] = rchop(nick,endings)

def clear_numbers(nick):
    if nick[len(nick) - 1].isdigit():
        return re.sub("\d+$","", nick)
    else:
        return nick

def scrape(index_url):
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    divTag = soup.find_all('div', {'class':'SummonerName'})
    for tag in divTag:
        aTags = tag.find_all('a')
        for tag in aTags:
            tag.text.replace(" ", "")
            if re.match("^[A-Za-z0-9_-]*$", tag.text):
                nick_arr.append(tag.text.lower())

def make_passwords(nick_arr):
    passwords = []
    for nick in nick_arr:
        if nick[len(nick) - 1].isdigit():
            passwords.append(nick)
            passwords.append(clear_numbers(nick) + "1")
            passwords.append(clear_numbers(nick) + "13")
            passwords.append(clear_numbers(nick) + "123")
            passwords.append(clear_numbers(nick) + "12345")
            passwords.append(clear_numbers(nick) + "321")
            passwords.append(clear_numbers(nick) + "95")
            passwords.append(clear_numbers(nick) + "96")
            passwords.append(clear_numbers(nick) + "97")
            passwords.append(clear_numbers(nick) + "98")
            passwords.append("12345")
            passwords.append("qwertyuiop")
            passwords.append("123456789")
        else:
            passwords.append(nick)
            passwords.append(nick + "1")
            passwords.append(nick + "13")
            passwords.append(nick + "123")
            passwords.append(nick + "12345")
            passwords.append(nick + "321")
            passwords.append(nick + "95")
            passwords.append(nick + "96")
            passwords.append(nick + "97")
            passwords.append(nick + "98")
            passwords.append("12345")
            passwords.append("qwertyuiop")
            passwords.append("123456789")
    return passwords

def make_combo(nick_arr, password_array):
    combo = []
    x = 0
    for (index, nick) in enumerate(nick_arr):
        for i in range (x , x + 13):
            combo.append(nick + ":" + password_array[i])
        x = x + 13
    return combo

def make_unique(nick_arr):
    return list(set(nick_arr))

def choose_random(nick_arr):
    intgr = randint(0,len(nick_arr))
    if not nick_arr[intgr] in used_nicks:
        global summoner_url
        summoner_url = nick_arr[intgr]
        used_nicks.append(nick_arr[intgr])
    else:
        choose_random(nick_arr)

def save_file(array):
    f = open('output.txt', 'a', encoding='utf-8')
    for nick in array:
        f.write('%s\n' % nick)
    f.close()

def lets_go():
    scrape(root_url + summoner_url)
    choose_random(nick_arr)
    print('Next')

for x in range(0, how_much):
    lets_go()

clean_my_shit(nick_arr, endings)
print(len(make_unique(nick_arr)))
print(len(make_passwords(make_unique(nick_arr))))
save_file(make_combo(make_unique(nick_arr), make_passwords(make_unique(nick_arr))))
k=input("Press any key... Check your output.txt")

from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this formate YYYY-MM-DD\n")
url = f"https://www.billboard.com/charts/hot-100/{date}/"

response  = requests.get(url= url)
class2="c-title"
soup = BeautifulSoup(response.text, 'html.parser')
music_tag = soup.select(selector=".o-chart-results-list-row .c-title")
music_list = []
for m in music_tag:
    x = m.getText()
    x = x.replace("\n", "")
    x = x.replace("\t", "")
    music_list.append(x)







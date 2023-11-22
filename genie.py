import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url1 = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20231123&hh=04&rtm=Y&pg=1'
url2 = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20231123&hh=04&rtm=Y&pg=2'
url3 = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20231123&hh=04&rtm=Y&pg=3'
url4 = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20231123&hh=04&rtm=Y&pg=4'
resp1 = requests.get(url1, headers = headers)
resp2 = requests.get(url2, headers = headers)
resp3 = requests.get(url3, headers = headers)
resp4 = requests.get(url4, headers = headers)
soup1 = BeautifulSoup(resp1.text, 'html.parser')
soup2 = BeautifulSoup(resp2.text, 'html.parser')
soup3 = BeautifulSoup(resp3.text, 'html.parser')
soup4 = BeautifulSoup(resp4.text, 'html.parser')


songs1 = soup1.findAll('a',{'class' : 'title ellipsis'})
songs2 = soup2.findAll('a',{'class' : 'title ellipsis'})
songs3 = soup3.findAll('a',{'class' : 'title ellipsis'})
songs4 = soup4.findAll('a',{'class' : 'title ellipsis'})
peoples1 = soup1.findAll('a',{'class':'artist ellipsis'})
peoples2 = soup2.findAll('a',{'class':'artist ellipsis'})
peoples3 = soup3.findAll('a',{'class':'artist ellipsis'})
peoples4 = soup4.findAll('a',{'class':'artist ellipsis'})
 
for song1, people1, i in zip(songs1, peoples1, range(0,50)):
	title = song1.text.replace('19금\n','' ).strip()
	name = people1.text
	print(str(i+1)+"위 "+title.strip()+" : "+name.strip())
for song2, people2, i in zip(songs2, peoples2, range(0,50)):
	title = song2.text.replace('19금\n','' ).strip()
	name = people2.text
	print(str(i+51)+"위 "+title.strip()+" : "+name.strip())
for song3, people3, i in zip(songs3, peoples3, range(0,50)):
	title = song3.text.replace('19금\n','' ).strip()
	name = people3.text
	print(str(i+101)+"위 "+title.strip()+" : "+name.strip())
for song4, people4, i in zip(songs4, peoples4, range(0,50)):
	title = song4.text.replace('19금\n','' ).strip()
	name = people4.text
	print(str(i+151)+"위 "+title.strip()+" : "+name.strip())
 
all_songs = []
for songs, people, start_rank in zip([songs1, songs2, songs3, songs4],
                                     [peoples1, peoples2, peoples3, peoples4],
                                     [1, 51, 101, 151]):
    for i, (song, people) in enumerate(zip(songs, people)):
        title = song.text.replace('19금\n', '').strip()
        name = people.text
        rank = start_rank + i
        all_songs.append({"Rank": rank, "Title": title, "Artist": name})

df = pd.DataFrame(all_songs)

df.to_excel("genie_top_200.xlsx", index=False)
from requests import get
from bs4 import BeautifulSoup
import difflib
import pandas as pd

celeb_names = []


for i in ["1","2"]:
	url = "https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page="+i
	response = get(url)
	html_soup = BeautifulSoup(response.text, 'html.parser')



	name_list = html_soup.find_all('h3',class_="lister-item-header")
	for name in name_list:
	  if name.find('a'):
	    celeb_names.append(name.find('a').text.strip())

df = pd.DataFrame({"Celebrity Name":celeb_names})
df.to_csv('celeb.csv')





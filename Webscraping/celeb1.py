import pandas as pd 
from requests import get
from bs4 import BeautifulSoup
import difflib
df=pd.read_csv('celeb.csv')

X=df['Celebrity_Name'].tolist()
#print(X)

cleaned_list=[]
for each in X:
	each=each.lower()
	each=each[::-1].replace(" ","-",1)[::-1]
	each=each.replace(" ","")
	
	cleaned_list.append(each)



images=[]
final_list=[]
for name in cleaned_list:
	l=[]
	url = "https://www.celebrities-galore.com/celebrities/"+name+"/personality-number/"
	response = get(url)
	html_soup = BeautifulSoup(response.text, 'html.parser')



	all_p = html_soup.find_all('p')
	for p in all_p:
	  l.append(p.text.strip())

	des="".join(l)
	final_list.append(des)

	if html_soup.find('div',attrs={'class': "photo-container"}):
		div=html_soup.find('div',attrs={'class': "photo-container"})

		images.append(div.find('img').get('src'))
	else:
		images.append("NONE")
		
print(len(final_list))
print(len(images))


df1 = pd.DataFrame({"Customer_Name":X,"Celebrity_des":final_list,"Image":images})
df1.to_csv('celeb2.csv')
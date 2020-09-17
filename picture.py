from bs4 import BeautifulSoup
import requests
import csv
import urllib

count = 1

for i in range(0,30):
	url = 'https://tieba.baidu.com/p/6368938216?pn={}'.format(i)
	response = requests.get(url)
	soup = BeautifulSoup(response.content.decode('utf-8'),'lxml')
	body = soup.find('div',class_='p_postlist')
	for each_picture in body.find_all('img',class_='BDE_Image'):
		img_url = each_picture.get('src')
		r = requests.get(img_url)
		with open("{}.jpg".format(count),"wb") as code:
			code.write(r.content)
		count+=1
	
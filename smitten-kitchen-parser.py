from bs4 import BeautifulSoup

import requests

r  = requests.get("http://smittenkitchen.com/blog/2014/12/twice-baked-potatoes-with-kale/")

data = r.text

soup = BeautifulSoup(data, "html5lib")

head_tag = soup.head

for string in soup.stripped_strings:
	print repr(string)
#div class="entry" is where the recipe starts

#def a find ingredients function
#def a find instructions function
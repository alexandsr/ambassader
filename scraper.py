import requests
from bs4 import BeautifulSoup

# Get all the subpage links
url = 'https://www.svenska-ambassaden.com/2.php?c=Sverige'
grab = requests.get(url)
soup = BeautifulSoup(grab.text, 'html.parser')
 
f = open("linklist.txt", "w")
for link in soup.find_all("a"):
   data = link.get('href')
   f.write(data)
   f.write("\n")
 
f.close()
g = open("linklist.txt", "r")
urls = g.readlines()
for i in urls:
    take = requests.get(urls[i])
    suppe = BeautifulSoup(take.text, 'html.parser')
    data = link.get('href')
    match = requests.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', link)
    out = open("emails.txt", "w")
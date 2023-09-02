import requests
import re
from bs4 import BeautifulSoup
import fileinput
import sys
email_pattern = r'.+\@.+\..+'

# Get all the subpage links
#url = 'https://www.svenska-ambassaden.com/2.php?c=Sverige'
#grab = requests.get(url)
#soup = BeautifulSoup(grab.text, 'html.parser')
 
#f = open("linklist.txt", "w")
#print('Writing links to embassy pages to file.')
#for link in soup.find_all("a"):
#   data = link.get('href')
#   f.write(data + "\n")
#print('Finished writing links to embassy pages.')
#f.close()


#for line in fileinput.input(['./linklist.txt'], inplace=True):
#    sys.stdout.write('https://www.svenska-ambassaden.com/{l}'.format(l=line))

g = open("linklist.txt", "r")
urls = g.readlines()
for i in urls:
   print(i)
   take = requests.get(i)
   soup = BeautifulSoup(take.text, 'html.parser')

   # Find all email addresses in the take variable using the regular expression pattern
   mydivs = soup.findAll('div')
   for div in mydivs: 
      with open('divs.txt', 'w') as d:
         d.write(div + '\n')
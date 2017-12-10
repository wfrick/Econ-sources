import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def EV_parser(url):
    #Takes a "Links for" post from Economist's View; returns recommended links
    
    # Use requests to get the contents
    headers = {'User-Agent':'Mozilla/5.0'}
    r = requests.get(url,headers=headers)

    # Get the text of the contents
    html_content = r.text

    # Find post contents
    tk = html_content.split('<div class="entry-content">')
    tk = tk[1].split('<p class="entry-footer">')
    content = tk[0]

    #Extract links
    soup = BeautifulSoup(content, 'lxml')
    assorted_links = soup.find_all('a')
    links = []
    for a in assorted_links:
        links.append(a['href'])

    return links
    

EV = pd.read_csv("EV_clean_links.csv")
urls = EV['URL']

links_sources = []
count = 0
for a in urls:
    count += 1
    print count
    try:
        recs = EV_parser(a)
        for b in recs:
            links_sources.append([b,a])
    except:
        continue
        

#Create a dataframe
df = pd.DataFrame(columns = ["URL","Recommender"])
for c in links_sources:
    df.loc[len(df)] = c

#Print dataframe shape, save to CSV
print df.shape
df.to_csv("Recs_from_EV.csv")

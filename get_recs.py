from api import bing
from keys import bing_key as key
import urllib2
import pandas as pd
import numpy as np

def bing_urls(sites, term, maximum):
    #Takes a list of sites, a search term, and a number of links of 1,000 or less
    #Returns a list of search results from Bing as a list of URLs
    #The max offset in Bing is 1,000 so maximum must be 1,000 or less
    
    count = 0
    clean_urls = []
    while count < maximum:        
        print "the count is " + str(count)
        #Get 30 URLs from Bing
        urls = bing(key, term,30,count,news=False,sites=sites)
        print type(urls)
        if type(urls) == list:
            print "Got some urls"
            #Redirect to actual URL
            for a in urls:
                try:
                    clean_urls.append(urllib2.urlopen(a).geturl())
                except:
                    "Error with redirect"
                    clean_urls.append(a)
                    continue
        else:
            print "Got a bing error of some kind"


        count += 30

    return clean_urls


#Get link recommendations from Marginal Revolution
sites = ['http://marginalrevolution.com']
year = 2008
master = []
while year < 2018:
    term = "assorted " + str(year)
    urls = bing_urls(sites,term,365)
    year += 1
    master = master + urls

#Create a dataframe
df = pd.DataFrame(columns = ["URL"])
for b in master:
    df.loc[len(df)] = b

#Print dataframe shape, save to CSV
print df.shape
df.to_csv("MR_assorted_links.csv")


#Get link recommendations from Economist's View
sites = ['http://economistsview.typepad.com/']
year = 2008
master = []
while year < 2018:
    term = "Links for " + str(year)
    urls = bing_urls(sites,term,365)
    year += 1
    master = master + urls

#Create a dataframe
df = pd.DataFrame(columns = ["URL"])
for b in master:
    df.loc[len(df)] = b

#Print dataframe shape, save to CSV
print df.shape
df.to_csv("EV_links.csv")

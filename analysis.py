from urlparse import urlparse
import numpy as np
import pandas as pd

def domain(url):
        #Get the domain for a url
	source = urlparse(url).netloc
	return source

def top_level(domain):
        #Get the top-level domain (dot com etc)
    result = domain.split('.')
    result = result[len(result)-1]
    return result

#Load links
MR = pd.read_csv("Recs_from_MR.csv")
EV = pd.read_csv("Recs_from_EV.csv")

#Add a column to link dfs with the domain
MR['Domain'] = MR['URL'].apply(domain)
EV['Domain'] = EV['URL'].apply(domain)

#Find most frequent domains overall
topMR = MR['Domain'].value_counts()
topMR = topMR[0:50]

topEV = EV['Domain'].value_counts()
topEV = topEV[0:50]

#Find the domains common to both lists
both_lists = []
for a in topMR.index:
        if a in topEV.index:
                both_lists.append(a)

print "Here are the domains in both blogs' top 50:"
print both_lists

#Look for top domains that aren't dot coms:

#Add a column with the top-level domain (.com, .org, etc.)
MR['Top level'] = MR['Domain'].apply(top_level)
EV['Top level'] = EV['Domain'].apply(top_level)

#Subset by domains not dot com
MR_sub = MR.loc[MR['Top level'] != 'com']
EV_sub = EV.loc[EV['Top level'] != 'com']

#Find most frequent domains not dot com
topMRsub = MR_sub['Domain'].value_counts()
topMRsub = topMRsub[0:30]

topEVsub = EV_sub['Domain'].value_counts()
topEVsub = topEVsub[0:30]

#Find the domains common to both lists
both_lists2 = []
for a in topMRsub.index:
        if a in topEVsub.index:
                both_lists2.append(a)

print "Here are the domains in both blogs' top 50 excluding dot coms:"
print both_lists2

#Look for links just from this year (2017)
MR_2017 = MR[MR.Recommender.str.contains("2017") == True]
EV_2017 = EV[EV.Recommender.str.contains("2017") == True]

#Find most frequent domains for 2017
topMR2017 = MR_2017['Domain'].value_counts()
topMR2017 = topMRsub[0:50]

topEV2017 = EV_2017['Domain'].value_counts()
topEV2017 = topEVsub[0:50]

#Find the domains common to both lists
both_lists3 = []
for a in topMR2017.index:
        if a in topEV2017.index:
                both_lists3.append(a)

print "Domains common to both blogs' top 30 for 2017"
print both_lists3
 

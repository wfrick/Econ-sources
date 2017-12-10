import pandas as pd
import numpy as np

#Remove duplicates & URLs that aren't link recommendations

#Load dataframes of link rec URLs
MR = pd.read_csv("MR_assorted_links.csv")
EV = pd.read_csv("EV_links.csv")
print MR.shape
print EV.shape

#Delete duplicates
MR = MR.drop_duplicates(subset="URL")
EV = EV.drop_duplicates(subset="URL")

#Delete rows that aren't link recs
MR = MR[MR.URL.str.contains("assorted") == True]

EV = EV[EV.URL.str.contains("links") == True]
EV = EV[EV.URL.str.contains("comments") == False]
EV = EV.sort('URL')

#Print size of lists:
print MR.shape
print EV.shape

#Save de-duped lists to CSV
MR.to_csv("MR_clean_links.csv")
EV.to_csv("EV_clean_links.csv")


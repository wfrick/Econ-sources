import httplib, urllib, base64, json #Bing
from keys import *

def bing(key,term,number_of_results,offset,news=False,sites=[]):
    #Takes a search term, number of results, offset
    #News = True means a Bing news search, else web search
    #Returns list of articles, format: [URL, headline]
    #Documentation: https://dev.cognitive.microsoft.com/docs/services

    count = 0
    sites_string = ' ('
    if len(sites) > 0:
        while count < len(sites):
            if count == len(sites) - 1:
                site = 'site:'+str(sites[count])
                sites_string = sites_string + site
            else:
                site = 'site:'+str(sites[count])+' OR '
                sites_string = sites_string + site
            count +=1
        term = term + sites_string
    
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': key,
    }

    params = urllib.urlencode({
        # Request parameters
        'q': term,
        'count': number_of_results,
        'offset': offset,
        'mkt': 'en-us',
        'safeSearch': 'Moderate'
        #'freshness': 'Month'
    })

    try:
        conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
        if news == True:
            conn.request("GET", "/bing/v7.0/news/search?%s" % params, "{body}", headers)
        else:
            conn.request("GET", "/bing/v7.0/search?%s" % params, "{body}", headers)

        response = conn.getresponse()
        data = response.read()
        conn.close()
        results = json.loads(data)
        print results
        #Return articles
        articles = []
        count = 0

        while count < number_of_results:
            if news == True:
                url = results['value'][count]['url']
            else:
                url = results['webPages']['value'][count]['url']
            articles.append(url)
            count +=1
        return articles
    except Exception as e:
        return e
        print("[Errno {0}] {1}".format(e.errno, e.strerror))





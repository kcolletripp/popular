import urllib2
import json
from .models import Target
#from bs4 import BeautifulSoup

#for other files: 
#import utils
#utils.get_wiki(target)

def get_wiki(target):
    url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/" + urllib2.quote(target.target_name) + "/daily/20160101/" + datetime.datetime.today().strftime('%Y%m%d')
    data = json.load(urllib2.urlopen(url))
    total_views = 0
    
    for item in data['items']:
        #print(item['views'])
        total_views += item['views']

    return total_views

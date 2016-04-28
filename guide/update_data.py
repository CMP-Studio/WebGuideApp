import requests
import pprint
#from guide.models import *

sync_url = "http://guidecms.carnegiemuseums.org/api/v2/sync"

# First we need to retrieve the data
r = requests.get(sync_url)
data = r.json()
#pretty print
print "Here is the JSON:"
pprint.pprint(data)
print vars(data)

def get_sync_data():
    global sync_url
    r = requests.get(sync_url)
    data = r.json()
    return data

import requests
import json
import pprint
#from guide.models import *

sync_url = "http://guidecms.carnegiemuseums.org/api/v2/sync"

# First we need to retrieve the data
print "Retrieving data from CMS..."
r = requests.get(sync_url)
data = r.json()
print "Done!"
print data.status
print "Processing exhibitions..."
pprint.pprint(data.exhibitions)

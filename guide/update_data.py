import requests
import json
import pprint
from guide.models import Exhibition

sync_url = "http://guidecms.carnegiemuseums.org/api/v2/sync"

# First we need to retrieve the data
print "Retrieving data from CMS..."
r = requests.get(sync_url)
data = r.json()
#check if data status is True
if data['status']:
    print "Done!"
else:
    print "Data is not good.  Exiting."
    sys.exit(0)

#Exhibitions
print "Processing Exhibitions..."
exhib = data['exhibitions']
Exhibition.objects.all().delete()
for key, e in exhib.items():
    pprint.pprint(e)
    exhib_obj = Exhibition(uuid=e.uuid, title=e.title)
    exhib_obj.save()

print "Exhibitions are complete"

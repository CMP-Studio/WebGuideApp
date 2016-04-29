import requests
import json
import pprint
from guide.models import Exhibition

#Functions
def import_items(obj, data):
    for key, value in data.iteritems():
        print str(key) + " = " + str(value)
        setattr(obj, key, value)


#Main
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
for e in exhib:
    exhib_obj = Exhibition()
    import_items(exhib_obj, e)
    exhib_obj.save()

print "Exhibitions are complete"

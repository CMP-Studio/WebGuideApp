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
for e in exhib:
    exhib_obj = Exhibition()
    fields = Exhibition._meta.get_fields()
    for f in fields:
        if type(f).__name__ = 'ManyToOneRel': #Skip relationships
            continue
        setattr(exhib_obj, f.name, e[f.name])
    exhib_obj.save()

print "Exhibitions are complete"

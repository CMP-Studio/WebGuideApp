import requests
import json
import pprint
from guide.models import Location, Category, Exhibition

#Functions
def import_items(obj, data):
    for key, value in data.iteritems():
        setattr(obj, key, value)


#Main
sync_url = "http://guidecms.carnegiemuseums.org/api/v2/sync"

# First we need to retrieve the data
print "\nRetrieving data from CMS..."
r = requests.get(sync_url)
data = r.json()
#check if data status is True
if data['status']:
    print "\nDone!"
else:
    print "\nData is not good.  Exiting."
    sys.exit(0)

#Location
print "\nProcessing Locations..."
entries = data['locations']
Location.objects.all().delete()
for e in entries:
    obj = Location()
    import_items(obj, e)
    obj.save()

#Category
print "\nProcessing Categories..."
entries = data['categories']
Category.objects.all().delete()
for e in entries:
    obj = Category()
    import_items(obj, e)
    obj.save()

#Exhibitions
print "\nProcessing Exhibitions..."
exhib = data['exhibitions']
Exhibition.objects.all().delete()
for e in exhib:
    exhib_obj = Exhibition()
    import_items(exhib_obj, e)
    exhib_obj.save()

#Category
print "\nProcessing Tours..."
entries = data['tours']
Tour.objects.all().delete()
for e in entries:
    obj = Tour()
    import_items(obj, e)
    obj.save()

import requests
import json
import pprint
from guide.models import Location, Category, Exhibition, Tour, Artist, Link

#Functions
def import_items(obj, data):
    for key, value in data.iteritems():
        if str(key).endswith("_uuid"):
            continue
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

#Tours
print "\nProcessing Tours..."
Tour.objects.all().delete()
entries = data['tours']
for e in entries:
    obj = Tour()
    if Exhibition.objects.filter(uuid=e['exhibition_uuid']):
        ex = Exhibition.objects.get(uuid=e['exhibition_uuid'])
    else:
        continue
    obj.exhibition = ex
    import_items(obj, e)
    obj.save()

#Artist
print "\nProcessing Artists..."
Artist.objects.all().delete()
entries = data['artists']
for e in entries:
    obj = Artist()
    if Exhibition.objects.filter(uuid=e['exhibition_uuid']):
        ex = Exhibition.objects.get(uuid=e['exhibition_uuid'])
    else:
        continue
    obj.exhibition = ex
    import_items(obj, e)
    obj.save()

#Links
print "\nProcessing Linkss..."
Link.objects.all().delete()
entries = data['links']
for e in entries:
    obj = Link()
    if Exhibition.objects.filter(uuid=e['exhibition_uuid']):
        ex = Exhibition.objects.get(uuid=e['exhibition_uuid'])
    else:
        continue
    obj.exhibition = ex
    if Artist.objects.filter(uuid=e['artist_uuid']):
        fk = Artist.objects.get(uuid=e['artist_uuid'])
    else:
        continue
    obj.artist = fk
    import_items(obj, e)
    obj.save()

print "Done!"

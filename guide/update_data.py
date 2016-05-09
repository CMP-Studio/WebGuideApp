import requests
import json
import pprint
import markdown
import re
from django.utils.text import slugify
from guide.models import Location, Category, Exhibition, Tour, Artist, Link, Artwork, Media, artistArtwork, tourArtwork

#Functions
def import_items(obj, data):
    for key, value in data.iteritems():
        if str(key).endswith("_uuid"):
            continue
        setattr(obj, key, value)

def get_html_from_markdown(text):
    text = re.sub('\r*\n','<br />', text)
    return markdown.markdown(text)


#Main
def update_from_CMS():
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
        obj.slug = slugify(e['title'])[:75]
        obj.save()

    #Exhibitions
    print "\nProcessing Exhibitions..."
    exhib = data['exhibitions']
    Exhibition.objects.all().delete()
    for e in exhib:
        obj = Exhibition()
        import_items(obj, e)
        obj.slug = slugify(e['title'])[:75]
        obj.save()

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
        obj.slug = slugify(e['title'])[:75]
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
        obj.slug = slugify(e['first_name'] + ' ' + e['last_name'])[:75]
        obj.save()

    #Links
    print "\nProcessing Links..."
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

    #Artwork
    print "\nProcessing Artwork..."
    Artwork.objects.all().delete()
    entries = data['artwork']
    for e in entries:
        obj = Artwork()
        if Exhibition.objects.filter(uuid=e['exhibition_uuid']):
            ex = Exhibition.objects.get(uuid=e['exhibition_uuid'])
        else:
            continue
        obj.exhibition = ex
        if Location.objects.filter(uuid=e['location_uuid']):
            fk = Location.objects.get(uuid=e['location_uuid'])
        else:
            continue
        obj.location = fk
        if Category.objects.filter(uuid=e['category_uuid']):
            fk = Category.objects.get(uuid=e['category_uuid'])
        else:
            continue
        obj.category = fk
        import_items(obj, e)
        obj.slug = slugify(e['code'] + ' ' + e['title'])[:75]
        obj.body_html = get_html_from_markdown(e['body'])
        obj.save()

    #Links
    print "\nProcessing Media..."
    Media.objects.all().delete()
    entries = data['media']
    for e in entries:
        obj = Media()
        if Exhibition.objects.filter(uuid=e['exhibition_uuid']):
            ex = Exhibition.objects.get(uuid=e['exhibition_uuid'])
        else:
            continue
        obj.exhibition = ex
        if Artwork.objects.filter(uuid=e['artwork_uuid']):
            fk = Artwork.objects.get(uuid=e['artwork_uuid'])
        else:
            continue
        obj.artwork = fk
        import_items(obj, e)
        obj.save()

    #ArtistArtwork
    print "\nProcessing Artist-Artwork links..."
    artistArtwork.objects.all().delete()
    entries = data['artistArtworks']
    for e in entries:
        obj = artistArtwork()
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
        if Artwork.objects.filter(uuid=e['artwork_uuid']):
            fk = Artwork.objects.get(uuid=e['artwork_uuid'])
        else:
            continue
        obj.artwork = fk
        import_items(obj, e)
        obj.save()

    #ArtistArtwork
    print "\nProcessing Tour-Artwork links..."
    tourArtwork.objects.all().delete()
    entries = data['tourArtworks']
    for e in entries:
        obj = tourArtwork()
        if Exhibition.objects.filter(uuid=e['exhibition_uuid']):
            ex = Exhibition.objects.get(uuid=e['exhibition_uuid'])
        else:
            continue
        obj.exhibition = ex
        if Tour.objects.filter(uuid=e['tour_uuid']):
            fk = Tour.objects.get(uuid=e['tour_uuid'])
        else:
            continue
        obj.tour = fk
        if Artwork.objects.filter(uuid=e['artwork_uuid']):
            fk = Artwork.objects.get(uuid=e['artwork_uuid'])
        else:
            continue
        obj.artwork = fk
        import_items(obj, e)
        obj.save()

    print "\nDone!"

if __name__ == "__main__":
    update_from_CMS()

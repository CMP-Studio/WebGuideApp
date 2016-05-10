import requests
import json
import pprint
import re
from guide.models import Hour


def update_hours_CMS():
    url = "http://guidecms.carnegiemuseums.org/api/v2/hours"
    print "\nRetrieving data from CMS..."
    r = requests.get(url)
    data = r.json()

    hours = data['hours']
    #Remove previous hours
    Hour.objects.all().delete()
    h = Hour()

    for key, value in data.iteritems():
        h.dow = key
        h.day_open = data[key]['open']
        h.day_close = data[key]['close']

    h.save()
    print "\nDone!"

if __name__ == "__main__":
    update_hours_CMS()

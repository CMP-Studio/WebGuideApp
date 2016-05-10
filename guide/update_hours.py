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
    dow = {"Sunday":1,"Monday":2,"Tuesday":3,"Wednesday":4,"Thursday":5,"Friday":6,"Saturday":7}

    for key, value in hours.iteritems():
        h = Hour()
        h.dow_i = dow[key]
        h.dow = key
        h.day_open = value['open']
        h.day_close = value['close']
        h.save()


    print "\nDone!"

if __name__ == "__main__":
    update_hours_CMS()

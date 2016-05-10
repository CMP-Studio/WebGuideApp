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
    #Remove previous hours
    Hour.objects.all().delete()
    h = Hour()
    h.date_requested    = data['requested_date']
    h.date_start        = data['date_range']['start']
    h.date_end          = data['date_range']['end']
    h.sunday_open       = data['hours']['Sunday']['open']
    h.sunday_close      = data['hours']['Sunday']['close']
    h.monday_open       = data['hours']['Monday']['open']
    h.monday_close      = data['hours']['Monday']['close']
    h.tuesday_open      = data['hours']['Tuesday']['open']
    h.tuesday_close     = data['hours']['Tuesday']['close']
    h.wednesday_open    = data['hours']['Wednesday']['open']
    h.wednesday_close   = data['hours']['Wednesday']['close']
    h.thursday_open     = data['hours']['Thursday']['open']
    h.thursday_close    = data['hours']['Thursday']['close']
    h.friday_open       = data['hours']['Friday']['open']
    h.friday_close      = data['hours']['Friday']['close']
    h.saturday_open     = data['hours']['Saturday']['open']
    h.saturday_close    = data['hours']['Saturday']['close']

    h.save()
    print "\nDone!"

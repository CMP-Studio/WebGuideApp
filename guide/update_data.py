import pprint
#from guide.models import *

sync_url = "http://guidecms.carnegiemuseums.org/api/v2/sync"

def update():
    # First we need to retrieve the data
    data = get_sync_data()
    #pretty print
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)

def get_sync_data():
    global sync_url
    r = requests.get(sync_url)
    data = r.json
    return data

if __name__ == "__main__": update()

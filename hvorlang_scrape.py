import numpy as np
import pandas as pd
import requests
import scraping_class
import time
import random
import json
import tqdm

logfile = 'Hvorlangterder_total_log.csv'
connector = scraping_class.Connector(logfile)

df = pd.read_csv('Boliga - Behandling 2 - Befolkningstal.csv')

def create_url_and_scrape(lat_long):
    url = 'https://hvorlangterder.poi.viamap.net/v1/nearestpoi/?poitypes='
    poitypes = ["lake", "forest", "doctor", "supermarket", "school", "daycare", "hospital", "metro",
                "train", "stop", "strain", "junction", "pharmacy", "library", "coast", "airport"]
    coor = lat_long.split(' ')
    coordinates = '&fromcoord=' + ''.join(coor)
    auth = '&mot=foot&token=eyJkcGZ4IjogImh2b3JsYW5ndGVyZGVyIiwgInByaXZzIjogInIxWjByMEYwazZCdFdxUWNPVXlrQi95NlNVcEp2MlFiZ3lYZXRxNEhZNFhPLzNZclcwK0s5dz09In0.fP4JWis69HmaSg5jVHiK8nemiCu6VaMULSGGJyK4D4PkWq4iA1+nSHWMaHxepKwJ83sEiy9nMNZhv7BcktRNrA'
    tempurl = url + ','.join(poitypes) + coordinates + auth
    #time.sleep(0.3)
    print(1)
    response, call_id = connector.get(tempurl,'Coordinates_datascience')
    js = response.json()
    data = dict()
    data['lake'] = js['lake']['routedmeters']
    data['forest'] = js['forest']['routedmeters']
    data['doctor'] = js['doctor']['routedmeters']
    data['supermarket'] = js['supermarket']['routedmeters']
    data['school'] = js['school']['routedmeters']
    data['daycare'] = js['daycare']['routedmeters']
    data['hospital'] = js['hospital']['routedmeters']
    data['metro'] = js['metro']['routedmeters']
    data['train'] = js['train']['routedmeters']
    data['strain'] =js['strain']['routedmeters']
    data['junction'] = js['junction']['routedmeters']
    data['pharmacy'] = js['pharmacy']['routedmeters']
    data['library'] = js['library']['routedmeters']
    data['coast'] = js['coast']['routedmeters']
    data['airport'] = js['airport']['routedmeters']
    return data
df['hvorlangt_total'] = df['coordinate'].apply(create_url_and_scrape)

df.to_csv('howlongdf2.csv')

# Get Your Facebook Access Token Here...
# https://developers.facebook.com/tools/explorer?method=GET&path=me&version=v3.2

# Before running this code...
# Set your Facebook Access Token as an environment variable in your terminal:
# set ACCESS_TOKEN={YOUR ACCESS TOKEN}

import json
from urllib.request import urlopen


host = "https://graph.facebook.com/"
params = "books"
ACCESS_TOKEN = 'YOUR ACCESS TOKEN here'
id = 'me'
url = host + id + '?fields=' + params + '&access_token=' + ACCESS_TOKEN

# open the URL and read the response
with urlopen(url) as response:
   resp = response.read()

# convert the returned JSON string to a Python data-type
data = json.loads(resp.decode('utf-8'))

out = data[params]['data']

# list of books name, id, time-created
name = []
id = []
time = []
for dic in out:
   book = dic
   name.append(dic['name'])
   id.append(dic['id'])
   time.append(dic['created_time'])
   print(book)

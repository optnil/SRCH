import urllib.request
import json
from .Entity.Result import Results

class GoogleFetch:

    def fetch(self, key):

        exampleSearch = key
        print('Searching web for '+key)
        # encoded = urllib.quote(exampleSearch)
        url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyD8-zQW_mMM-dOyny75J0RdRDgyMP1P8hw&cx=003369086800144489281:fnxwb3klqza&q='
        urlup = url+key
        rawData = urllib.request.urlopen(urlup).read()
        jsonData = json.loads(rawData)
        links=[]

        for i in range(10):
            link = json.dumps(jsonData['items'][i]['link'], indent=4)
            snippet = json.dumps(jsonData['items'][i]['snippet'], indent=4)
            title = json.dumps(jsonData['items'][i]['title'], indent=4)
            ele = Results(title.strip('"\''), link.strip('"\''), snippet.strip('"\''), 2)
            links.append(ele)
        for i in range(10):
            print(links[i].name)
        return links

#obj = GoogleFetch()
#bj.fetch("Dog")

from django.shortcuts import render

from django.template import loader
import http.client, urllib.parse, json
from .forms import NameForm


from .joinResult import joinR
import urllib
subscriptionKey = "3ff2d1ad65c34ec884f8d30326cf623f"
host = "api.cognitive.microsoft.com"
path = "/bing/v7.0/search"

term = "Dog"


def index(request):

    template=loader.get_template('SearchEngine/index.html')
    if len(subscriptionKey) == 32:

        print('Searching the Web for: ', term)

        headers, result = BingWebSearch(term)
        print("\nRelevant HTTP Headers:\n")
        print("\n".join(headers))
        print("\nJSON Response:\n")
        res = json.loads(result);

        return render(request, 'SearchEngine/index.html', {
            'url1': res['webPages']['value']
        })


def BingWebSearch(search):
        "Performs a Bing Web search and returns the results."

        headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
        conn = http.client.HTTPSConnection(host)
        query = urllib.parse.quote(search)
        conn.request("GET", path + "?q=" + query, headers=headers)
        response = conn.getresponse()
        headers = [k + ": " + v for (k, v) in response.getheaders()
                   if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]
        return headers, response.read().decode("utf8")

def homepage(request):
    template=loader.get_template('SearchEngine/homepage.html')
    return render(request,'SearchEngine/homepage.html')

def get_name(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            search=form.cleaned_data['search']
            print(search)
            str(request.body, encoding='utf-8')
            if len(subscriptionKey) == 32:
                print('Searching the Web for: ', search)

                ob = joinR()

                return render(request, 'SearchEngine/index.html', {

                    'url1': ob.merge(search), 'search':search
                })









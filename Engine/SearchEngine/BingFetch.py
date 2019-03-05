

import http.client, urllib.parse, json


# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the subscriptionKey string value with your valid subscription key.
from .Entity.Result import Results

subscriptionKey = "09271addeb51437ba4bfa05f36471be4"

# Verify the endpoint URI.  At this writing, only one endpoint is used for Bing
# search APIs.  In the future, regional endpoints may be available.  If you
# encounter unexpected authorization errors, double-check this value against
# the endpoint for your Bing Web search instance in your Azure dashboard.
class BingFetch:


    def BingWebSearch(self, search):
        "Performs a Bing Web search and returns the results."

        host = "api.cognitive.microsoft.com"
        path = "/bing/v7.0/search"
        headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
        conn = http.client.HTTPSConnection(host)
        query = urllib.parse.quote(search)
        conn.request("GET", path + "?q=" + query, headers=headers)
        response = conn.getresponse()
        headers = [k + ": " + v for (k, v) in response.getheaders()
                       if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]
        return headers, response.read().decode("utf8")
    def bing(self,term):


        if len(subscriptionKey) == 32:

            print('Searching the Web for: ', term)


            headers, result = self.BingWebSearch(term)
            print("\nRelevant HTTP Headers:\n")
            print("\n".join(headers))
            print("\nJSON Response:\n")
            res = json.loads(result);
            links = []
            for i in range(10):
                name = json.dumps(res['webPages']['value'][i]['name'], indent=4)
                url = json.dumps(res['webPages']['value'][i]['url'], indent=4)
                detail = json.dumps(res['webPages']['value'][i]['snippet'], indent=4)
                ele = Results(name.strip('"\''), url.strip('"\''), detail.strip('"\''), 1)

                links.append(ele)
            return links
            for i in range(10):
                print(links[i].link)

        else:

            print("Invalid Bing Search API subscription key!")
            print("Please paste yours into the source code.")

# b = BingFetch()
# b.bing()
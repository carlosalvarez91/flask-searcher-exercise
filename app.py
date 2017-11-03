import pprint
import json
import random
from flask import Flask, render_template
from googleapiclient.discovery import build
#custom search engine ID 000201262982528788274:btxholjtuq0
#api key AIzaSyDjCVuiMp4eT0wLrRlGhmD7DsU_h8f7a-I

#https://github.com/google/google-api-python-client/blob/master/samples/customsearch/main.py
def custom_search():
    service = build(
        "customsearch",
        "v1",
        developerKey="AIzaSyABO4RjWa3GQSu11Sa9Y6FKy48rth4v_rs"
        )
    array =['Man', 'Mountain', 'State', 'Ocean', 'Country', 'Building', 'Cat', 'Airline', 'Wealth', 'Happiness', 'Pride', 'Fear', 'Religion', 'Bird', 'Book', 'Phone', 'Rice', 'Snow', 'Water']
    array_random = random.choice(array)#choice randomly a value from the array
    res = service.cse().list(
        #https://developers.google.com/custom-search/json-api/v1/reference/cse/list
        q=array_random,
        cx='000201262982528788274:btxholjtuq0',
        searchType='image', #Specifies the search type: image
        #imgDominantColor='', #Returns images of a specific dominant color. Get param from body
        num=5,#Number of search results to return.
    ).execute()
    res_json = json.dumps(res,sort_keys=True, indent=4)#encoding res to json
    return (res['items'], res_json)

#extract the 'link' value from res['items']
res_links = custom_search()[0]
for res_link in res_links:
    print(res_link.get('link'))

#extract the 'searchTime' value from res_json
results = json.loads(custom_search()[1])#parse json
searchTime = results['searchInformation']['searchTime'] # extract 'searchTime' value
print(searchTime)


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
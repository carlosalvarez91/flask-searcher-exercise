import json
import random
from flask import Flask, render_template, request
from googleapiclient.discovery import build
#custom search engine ID 000201262982528788274:btxholjtuq0
#api key AIzaSyDjCVuiMp4eT0wLrRlGhmD7DsU_h8f7a-I
app = Flask(__name__)


@app.route('/search' , methods=[ 'POST'])
#https://github.com/google/google-api-python-client/blob/master/samples/customsearch/main.py
def custom_search():
    #request select value to string
    select = request.form.get('colors')
    select_str=str(select)
    print(select_str)
    # google custom search API
    service = build(
        "customsearch",
        "v1",
        developerKey="AIzaSyABO4RjWa3GQSu11Sa9Y6FKy48rth4v_rs"
        )
    #array of words
    array =['Man', 'Mountain', 'State', 'Ocean', 'Country', 'Building', 'Cat', 'Airline', 'Wealth', 'Happiness', 'Pride', 'Fear', 'Religion', 'Bird', 'Book', 'Phone', 'Rice', 'Snow', 'Water']
    array_random = random.choice(array)#choice randomly a value from the array
    res = service.cse().list(
        #https://developers.google.com/custom-search/json-api/v1/reference/cse/list
        q=array_random + select_str,
        cx='000201262982528788274:btxholjtuq0',
        searchType='image', #Specifies the search type: image
        #imgDominantColor=select_str, #Returns images of a specific dominant color. Get param from body
        num=5,#Number of search results to return.
    ).execute()
    res_items = res['items']#extract the 'items' values from res
    res_json = json.dumps(res,sort_keys=True, indent=4)#encoding res to json
    results = json.loads(res_json)#parse json
    searchTime = results['searchInformation']['searchTime'] # extract 'searchTime' value
    return render_template('home.html',res_items=res_items, searchTime=searchTime)

@app.route('/')
def index():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
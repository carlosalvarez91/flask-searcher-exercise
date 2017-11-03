import pprint
from flask import Flask, render_template
from googleapiclient.discovery import build
#custom search engine ID 000201262982528788274:btxholjtuq0
#api key AIzaSyDjCVuiMp4eT0wLrRlGhmD7DsU_h8f7a-I

#https://github.com/google/google-api-python-client/blob/master/samples/customsearch/main.py
def main():
  service = build("customsearch", "v1",
            developerKey="AIzaSyABO4RjWa3GQSu11Sa9Y6FKy48rth4v_rs")
#https://developers.google.com/custom-search/json-api/v1/reference/cse/list
  res = service.cse().list(
      q='hello',
      cx='000201262982528788274:btxholjtuq0',
      searchType='image', #Specifies the search type: image
      #imgDominantColor='', Returns images of a specific dominant color. Get param from body
      num=1,#Number of search results to return.
    ).execute()
  pprint.pprint(res)

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')

main()
if __name__ == '__main__':
    app.run(debug=True)
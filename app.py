import pprint
from flask import Flask, render_template
from googleapiclient.discovery import build
#custom search engine ID 000201262982528788274:btxholjtuq0
#api key AIzaSyDjCVuiMp4eT0wLrRlGhmD7DsU_h8f7a-I

def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build("customsearch", "v1",
            developerKey="AIzaSyABO4RjWa3GQSu11Sa9Y6FKy48rth4v_rs")

  res = service.cse().list(
      q='lectures',
      cx='000201262982528788274:btxholjtuq0',
    ).execute()
  pprint.pprint(res)

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')

main()
if __name__ == '__main__':
    app.run(debug=True)
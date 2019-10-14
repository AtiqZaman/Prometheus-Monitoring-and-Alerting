from flask import json
from flask import request
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to Flask http server"


@app.route('/prometheus', methods=['POST'])
def webhook_api_prometheus():
    if request.headers['Content-Type'] == 'application/json':
        print ("json file received ")
        my_date = json.dumps(request.json)
        print (my_date)
        subprocess.Popen(["bash", "/home/atiq/testScript.sh"]) 
                                  #Here you have to provide your script path and script name
        return (my_date)

#@app.route('/github', methods=['POST'])
#def api_github_message():
#    if request.headers['Content-Type'] == 'application/json':
#        print ("Great, you got the json data")
#        my_info = json.dumps(request.json)
#        print (my_info)
#        return (my_info)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)

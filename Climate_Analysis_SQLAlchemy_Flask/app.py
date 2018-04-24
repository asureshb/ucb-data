#!/usr/local/bin/python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    print("This is Climate Data Analysis webservice")

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0', port=9090)

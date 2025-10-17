#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <form action="/echo_user_input" method="POST">
         <label for="user_input">County:</label>
         <input type="text" id="user_input" name="user_input">
         <input type="submit" value="Submit!">
     </form>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    data = get_incentives_db(input_text)
    return "Incentives for " + input_text + " County: " + data["Name"]


def get_incentives_db(name):
    data = {
    "Name": "Alameda Municipal Power - Electric Vehicle Rebate Program",
    "State": "CA",
    "Category": "Financial Incentive",
    "IncentiveType": "Rebate Program",
    "Created": "07/02/2021",
    "Updated": "01/28/2025" 
    }
    return data


from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"url{name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"url{name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", person_name=name)



if __name__ == "__main__":
    app.run(debug=True)
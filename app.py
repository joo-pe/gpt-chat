from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm
import openai
import json

openai.api_key = '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'

app = Flask(__name__)
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": request.args.get('sendMsg')}]
        )
        print(completion.get('choices')[0].get('message').get('content'))
    return render_template("index.html", result=completion.get('choices')[0].get('message').get('content'))

if __name__ == '__main__':
    app.run(debug=True)
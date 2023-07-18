
from flask import Flask,request,render_template,url_for
from Crypto.Random import get_random_bytes
import os

app = Flask(__name__)
app.secret_key = get_random_bytes(16)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    try:
        command = request.args.get("search")
        file = open(command).read()  #LFI Vulnerbility unsanitized data
    except Exception as e:
        file = f'{str(e)}'
    return render_template("index.html",data=file)     
    
@app.route("/fix")
def fix():
    try:
        command = request.args.get("search")
        file_path = os.getcwd() + "/static/" # Define allowed directory
        if file_path not in command or '../' in command:
            file = 'Malicious File Path Detected'
        else:
            file = open(command).read() # Else run open file
    except Exception as e:
        file = f'{str(e)}'
    return render_template("index.html",data=file)
     
app.run('0.0.0.0',8000)



from flask import Flask, request,render_template
from waitress import serve
import time as t
import threading as th
from flask_cors import CORS
import ip
app = Flask(__name__)
CORS(app)
light = 1

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/uno",methods = ["POST"])
def uno():
    global light
    light = request.form["led"]
    return "success"
@app.route("/temperature")
def temperature():
    global light
    return str(light)
def add():
    global light
    while True:
        t.sleep(1.5)
        light += 1

if __name__ == "__main__":
    print("Listening")
    # thread = th.Thread(target = add)
    # thread.start()
    serve(app, host = ip.ip, port=ip.port)
    

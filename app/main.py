from flask import Flask, render_template, request
from waitress import serve
import chat

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form", methods=["POST"])
def form():
    global cnt
    f = request.files["picture"]
    fileName = "./pictures/picture"+str(cnt)
    f.save(fileName)
    cnt += 1
    ret = chat.chatImage(fileName)
    return render_template("form.html", ret=ret) 
    
if __name__ == "__main__":
    cnt = 0
    serve(app, host="0.0.0.0", port=443)

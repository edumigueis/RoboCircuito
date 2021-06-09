from flask import Flask, request, Response, render_template, session, redirect
import webbrowser
import os

app = Flask(__name__)

@app.route('/')
def img():
        return render_template("index.html")

@app.route('/api/img', methods=['POST'])
def img_post():
    url = os.path.dirname(os.path.abspath(__file__)) + "/controllers/4wheels/photo.png"
    webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)
    return Response(status= 200)

# start flask app
app.run(host="localhost", port=5000)
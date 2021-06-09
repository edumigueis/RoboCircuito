from flask import Flask, request, Response, render_template, session

# Initialize the Flask application
app = Flask(__name__)

# route http posts to this method

@app.route('/api/img')
def ret():
    session['image'] = 'https://images.pexels.com/photos/2693212/pexels-photo-2693212.png?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940'
    return render_template("index.html", image = session.get('image', None))

@app.route('/api/img', methods=['POST'])
def img():
    r = request.get_json()["img"]
    print(r);
    return render_template("index.html", image = r)


# start flask app
app.run(host="localhost", port=5000)
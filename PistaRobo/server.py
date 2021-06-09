from flask import Flask, request, Response, render_template, session, redirect

app = Flask(__name__)

@app.route('/api/img/<i>', methods=['GET'])
def img(i):
    if i == None:
        return render_template("index.html", image = "https://images.pexels.com/photos/2693212/pexels-photo-2693212.png?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940")
    else:
        return render_template("index.html", image = i)

@app.route('/api/img', methods=['POST'])
def img_post():
    r = request.get_json()["img"]
    print(r);
    return redirect(f"/api/img/{r}")

# start flask app
app.run(host="localhost", port=5000)
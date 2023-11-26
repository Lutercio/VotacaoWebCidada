from flask import Flask, render_template, request, redirect

app = Flask(__name__)

votes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resultado")
def resultado():
    return render_template("resultado.html", votes=votes)

@app.route("/voto", methods=["POST"])
def voto():
    selection = int(request.form.get("option"))
    votes[selection] += 1
    print(selection)
    print(votes)
    return redirect("/resultado")
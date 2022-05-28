from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret'

@app.route('/')
def index():
    return render_template("index.html")

# Have the '/result' route display the information from the form on a new HTML page
@app.route('/result')
def result():
    if not 'name' in session:
        session['name'] = null
    if not 'location' in session:
        session['location'] = null
    if not 'fav_language' in session:
        session['fav_language'] = null
    if not 'comment' in session:
        session['comment'] = null
    return render_template("result.html",ninja=session['name'],dojo=session['location'],language=session['fav_language'],comments=session['comment'])


@app.route('/process_result',methods=["POST"])
def process_result():
    session["name"]= request.form["ninjaName"]
    session["location"] = request.form["dojoLocation"]
    session["fav_language"] = request.form["favLanguage"]
    session["comment"] = request.form["comment"]
    return redirect("/result")

if __name__ == "__main__":
    app.run(debug = True)
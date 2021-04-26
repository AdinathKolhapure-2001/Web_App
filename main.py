from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("template.html")

@app.route("/Home")
def home_1():
    return render_template("home.html")

@app.route("/About")
def about_flask():
    return render_template("about.html")

@app.route("/myName")
def name():
    return "My Name is Adinath"
    
if __name__=="__main__":
    app.run(debug=True)
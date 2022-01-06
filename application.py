import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    if request.method == "POST":
        if topic == None:
            return redirect("/tools")
    else:
        return render_template("index.html") 

@app.route("/tools", methods=["GET", "POST"])
def tools():
    topic = request.form.get("topic")
    if not topic:
        return redirect("/")

    print(topic)
    return render_template("tools.html", t=request.form.get("topic","nope"))

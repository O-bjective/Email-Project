from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask_oauthlib.client import OAuth
from flask import render_template

import pprint
import os
import json
#os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app = Flask(__name__)

app.debug = True #Change this to False for production

app.secret_key = os.environ['SECRET_KEY'] #used to sign session cookies
oauth = OAuth(app)
@app.route('/', methods=["POST","GET"])
def renderStore():
    if "itemsincart" not in session or "clear" in request.args:
        session["itemsincart"] = 0
        print("skrt")
        session["item_a"] = 0
        session["item_b"] = 0
        session["item_c"] = 0


    return render_template("home.html",itemsincart=session["itemsincart"])


@app.route('/Page1',methods=["POST","GET"])
def renderAddToCart():
    session["itemsincart"] += 1
    if request.args["item"]=="a":
        session["item_a"] += 1

    elif request.args["item"]=="b":
        session["item_b"] += 1

    elif request.args["item"]=="c":
        session["item_c"] += 1
    return render_template("Page1.html", item_name = "Item" + str(request.args["item"]))

@app.route('/Page2',methods=["POST","GET"])
def renderCheckout():
    if "itemsincart" not in session:
        return redirect(url_for("renderStore"))
    return render_template("Page2.html",itemsincart=session["itemsincart"])

@app.route('/Page3',methods=["POST","GET"])
def renderBought():
    if "itemsincart" not in session:
        return redirect(url_for("renderStore"))
    items = session["itemsincart"]
    session["itemsincart"] = 0
    return render_template("Page3.html",itemsincart=str(items))

if __name__=="__main__":
    app.run(debug=True)

import os
import requests
import random

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

from helpers import apology, lookup, lookup_random

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/random", methods=["GET", "POST"])
def randomize():
    if request.method == "POST":  
        id = random.randint(1, 892)
        pokemon_data = lookup_random(id)
        return render_template("random.html", data=pokemon_data) 

@app.route("/", methods=["GET", "POST"])
def search_pokemon():
    # POST
    if request.method == "POST":
        # Validate - if pokemon_name is not found in API
        if not request.form.get("search").lower():
            return apology("missing pokemon name", 403)
        # User input text as lookup pokemon name
        # Form validation - making user input from search form lower case
        pokemon_data = lookup(request.form.get("search").lower().strip())
        if not pokemon_data:
            return apology("please input a valid pokemon", 403) 

        return render_template("pokemon.html", data=pokemon_data)

    else:
        return render_template("index.html")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
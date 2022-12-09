import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    return render_template("apology.html", top=code, bottom=message)

def lookup(name):
    """Look up pokemon."""

    # Contact API
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    except requests.RequestException as e:
        print(e)
        return None

    # Parse response
    try:
        info = response.json()
                
        names = info["forms"][0]["name"]
        types_list = info["types"]
        picture = info["sprites"]["other"]["official-artwork"]["front_default"]

        types = []
        for type_info in types_list:
            types.append(type_info.get("type").get("name"))

        return {
            "names": names, 
            "types": types, 
            "picture": picture
                }

    except (KeyError, TypeError, ValueError) as e:
        print(e)
        return None

def lookup_random(id):
    
    # Contact API
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    except requests.RequestException as e:
        print(e)
        return None

    # Parse response
    try:
        info = response.json()

        names = info["forms"][0]["name"]
        types_list = info["types"]
        picture = info["sprites"]["other"]["official-artwork"]["front_default"]

        types = []
        for type_info in types_list:
            types.append(type_info.get("type").get("name"))

        return {
            "names": names, 
            "types": types, 
            "picture": picture
                }

    except (KeyError, TypeError, ValueError) as e:
        print(e)
        return None
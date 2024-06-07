import random

from flask import Blueprint, render_template
import csv

e_commerce = Blueprint("e_commerce", __name__)


@e_commerce.route("/")
def home():
    with open("Productos.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    return render_template("index.html", data=data)
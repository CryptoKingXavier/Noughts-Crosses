from typing import Literal
from flask import Blueprint, render_template


main: Blueprint = Blueprint("main", __name__)


@main.get("/")
def index() -> tuple[str, Literal[200]]: return render_template("index.html"), 200

from flask import Blueprint, request, render_template, redirect
from db import get_db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET"])
def login():
    username = request.args.get("username", "")
    password = request.args.get("password", "")

    conn = get_db()
    cursor = conn.cursor()

    query = (
        "SELECT id FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + password
        + "'"
    )
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        return redirect("/dashboard?user_id=" + str(user[0]))
    return "Login failed"


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    username = request.form.get("username", "")
    password = request.form.get("password", "")
    tea_type = request.form.get("tea_type", "")
    sugar = request.form.get("sugar", "")
    extras = ", ".join(request.form.getlist("extras"))
    notes = request.form.get("notes", "")

    conn = get_db()
    cursor = conn.cursor()

    query = (
        "INSERT INTO users VALUES (NULL, '"
        + username
        + "', '"
        + password
        + "', '"
        + tea_type
        + "', '"
        + sugar
        + "', '"
        + extras
        + "', '"
        + notes
        + "')"
    )
    cursor.execute(query)
    conn.commit()
    conn.close()

    return redirect("/")

from flask import Blueprint, request, render_template
from db import get_db

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard")
def show_dashboard():
    user_id = request.args.get("user_id", "")

    conn = get_db()
    cursor = conn.cursor()

    query = (
        "SELECT username, tea_type, sugar, extras, notes FROM users WHERE id = "
        + user_id
    )
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if not user:
        return "User not found"

    return render_template(
        "dashboard.html",
        username=user[0],
        tea_type=user[1],
        sugar=user[2],
        extras=user[3],
        notes=user[4],
    )

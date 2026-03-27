from flask import Blueprint, request, render_template, redirect
import sqlite3

admin = Blueprint("admin", __name__)

DB_NAME = "users.db"


# ---------------- ADMIN LIST (tiles)
@admin.route("/admin")
def admin_panel():
    username = request.args.get("username", "")

    # ❌ Weak auth (intentional)
    if username != "admin":
        return "Access denied"

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Only fetch id + username (clean UI)
    cursor.execute("SELECT id, username FROM users")
    users = cursor.fetchall()

    conn.close()

    return render_template("admin.html", users=users)


# ---------------- USER DETAIL PAGE (XSS triggers here)
@admin.route("/admin/user")
def admin_user_detail():
    username = request.args.get("username", "")
    user_id = request.args.get("id", "")

    # ❌ Weak auth
    if username != "admin":
        return "Access denied"

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # ❌ IDOR + SQLi
    query = "SELECT username, tea_type, sugar, extras, notes FROM users WHERE id = " + user_id
    cursor.execute(query)
    user = cursor.fetchone()

    conn.close()

    if not user:
        return "User not found"

    return render_template(
        "admin_user.html",
        user_id=user_id,
        username=user[0],
        tea_type=user[1],
        sugar=user[2],
        extras=user[3],
        notes=user[4]
    )


# ---------------- DELETE USER
@admin.route("/delete_user")
def delete_user():
    user_id = request.args.get("id")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # ❌ SQLi + no auth
    cursor.execute("DELETE FROM users WHERE id = " + user_id)
    conn.commit()
    conn.close()

    return redirect("/admin?username=admin")
from flask import Flask, render_template, redirect, session
from db import init_db

from routes.auth import auth
from routes.dashboard import dashboard
from routes.attack import attack
from routes.admin import admin

app = Flask(__name__)

# 🔁 Mode toggle config
app.config["MODE"] = "insecure"

# 🔐 Required for sessions (secure mode)
app.secret_key = "supersecretkey"

# 🗄️ Initialize DB
init_db()


# 🏠 Home (Login page)
@app.route("/")
def home():
    # 🔥 If user is logged in → don't show login page
    if session.get("user_id"):
        return redirect("/dashboard")

    return render_template("login.html", mode=app.config["MODE"])


# 🔄 Toggle Route (UPDATED)
@app.route("/toggle")
def toggle_mode():
    if app.config["MODE"] == "insecure":
        app.config["MODE"] = "secure"
    else:
        app.config["MODE"] = "insecure"

    # ✅ Redirect to login page after switching
    return redirect("/")


# 📦 Register routes
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(attack)
app.register_blueprint(admin)


if __name__ == "__main__":
    app.run(debug=True)
    
@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store"
    return response
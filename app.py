from flask import Flask, render_template
from db import init_db

from routes.auth import auth
from routes.dashboard import dashboard
from routes.attack import attack
from routes.admin import admin

app = Flask(__name__)

init_db()


@app.route("/")
def home():
    return render_template("login.html")


# Register routes
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(attack)
app.register_blueprint(admin)

if __name__ == "__main__":
    app.run(debug=True)

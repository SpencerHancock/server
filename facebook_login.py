from flask import Flask, redirect, url_for
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook

app = Flask(__name__)
app.secret_key = "supersekrit"
blueprint = make_facebook_blueprint(
    client_id="1859379074131895",
    client_secret="859d5303fbff8fc7bedffaf9f78ece03",
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
	return "please work!"

@app.route("/login")
def login():
    if not facebook.authorized:
        return redirect(url_for("facebook.login"))
    resp = facebook.get("account/settings.json")
    assert resp.ok
    return "You are @{screen_name} on facebook".format(screen_name=resp.json()["screen_name"])

if __name__ == "__main__":
    app.run()
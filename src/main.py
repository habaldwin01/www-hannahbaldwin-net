from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix
import os

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

from site_controller import site_pages
app.register_blueprint(site_pages)

@app.errorhandler(404)
def not_found_error_handler(e):
    return render_template("404.jinja.html")

@app.route("/")
def home_screen():
    return render_template("index.jinja.html")

if __name__ == "__main__":
    app.run()

from flask_login import login_required, current_user
from werkzeug.exceptions import HTTPException
import os
from flask import abort, render_template, request, redirect, url_for, Blueprint
import json

main_bp = Blueprint("main", __name__)


# @main_bp.before_request
# def check():
#     if status["up"] is False and request.referrer is None:
#         return render_template("errors/404.html"), 404
#     elif status["maintenance"] is True and request.referrer is None:
#         return render_template("errors/523.html"), 523


# @main_bp.after_request
# def logRequest(response):
#     if status["logging"] is True:
#         ...
#     return response


@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect('/dashboard')
    return render_template('index.html')


@main_bp.route("/adminconsole", methods=["GET"])
@login_required
def handleAdminConsole():
    abort(401)


@main_bp.route("/login", methods=["GET"])
def handleLogin():
    return url_for("auth.login")


@main_bp.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    return render_template("dashboard.html")


@main_bp.errorhandler(HTTPException)
def handleError(e):
    if os.path.exists(os.path.join(os.getcwd(), "templates", "errors", f"{e.code}.html")):
        return render_template(f"errors/{e.code}.html"), e.code
    else:
        return render_template("errors/error.html"), e.code


from flask import (render_template, redirect, url_for,
                   request, current_app)
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app import login_manager
# from app.common.mail import send_email
from . import auth_bp
# from .forms import SignupForm, LoginForm
# from .models import User


@auth_bp.route('/')
def home():
    return render_template("login.html")
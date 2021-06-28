
from flask import abort, render_template

from app.models import Post
from . import docs_bp


@docs_bp.route("/dashboard")
def index():
    posts = Post.get_all()
    return render_template("pages/dashboard.html", posts=posts)



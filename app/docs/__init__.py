
from flask import Blueprint

docs_bp = Blueprint('docs', __name__, template_folder='templates')

from . import routes

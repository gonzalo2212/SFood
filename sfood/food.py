from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from sfood.auth import login_required
from sfood.db import get_db

bp = Blueprint('food', __name__)

@bp.route('/')
def index():
    db = get_db()

    return render_template('food/index.html')

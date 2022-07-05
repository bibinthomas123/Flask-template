from flask import flash, render_template, Blueprint, url_for, request , jsonify
from .model import User ,Note
from flask_sqlalchemy import SQLAlchemy
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required,  current_user
import json

views = Blueprint('views', __name__)


@views.route("/",  methods=['GET', 'POST'])
@login_required
def home():
    return render_template("todo.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    return jsonify({})
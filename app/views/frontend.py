from flask import Flask, render_template, flash, redirect, url_for, Blueprint
from flask import request, jsonify, helpers
from flask_security import Security, login_required
from app.views import api


frontend = Blueprint('frontend', __name__)


@frontend.route('/')
@frontend.route('/index')
@login_required
def index():
    return render_template("index/index.html", title="Test")

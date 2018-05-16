from flask import Flask, render_template, flash, redirect, url_for, Blueprint
from flask import request, jsonify, helpers, session, after_this_request
from flask_security import login_required
from app.views import api
from flask import abort
from flask_login import current_user

from app.security import security, user_datastore
from database import loadSession
from database import models
from configuration import config as cf
from flask_security.utils import login_user, get_post_login_redirect

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
@frontend.route('/index')
def index():
    return render_template("index.html", eth_wallet=cf.ACCOUNT_ADDRESS)


@frontend.route('/organisation')
@login_required
def organisation():
    return render_template("organisation.html", eth_wallet=cf.ACCOUNT_ADDRESS)


@frontend.route('/user_dashboard')
@login_required
def user_dashboard():
    session = loadSession()
    if (not current_user.is_authenticated):
        abort(500)

    user_id = current_user.id
    documents = session.query(models.NationalDocument).filter_by(user_id=user_id).all()
    certificates = []
    for doc in documents:
        certificates.extend(session.query(models.Certificate).filter_by(personal_document_id=doc.document_number,
                                                                        personal_document_type_code=doc.document_type_code).all())
    for cert in certificates:
        cert.org_name = session.query(models.Organisation).filter_by(
            ethereum_wallet=cert.organisation_ethereum_wallet).first().name

    return render_template("user_dashboard.html", certificates=certificates)

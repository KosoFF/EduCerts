from flask import Flask, render_template, flash, redirect, url_for, Blueprint
from flask import request, jsonify, helpers, abort
api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/get_project_systems',
           methods=['GET'])  # Can return project list if no args and single project with project id
def get_hello():
    """return project systems by project_id"""

    return jsonify(result="Hello world")

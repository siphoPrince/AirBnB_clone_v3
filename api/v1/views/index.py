#!/usr/bin/python3
"""
 route /status on the app_views Blueprint,
 and when this route is accessed via a
 GET request, it returns a JSON response with
 the content {"status": "OK"}
 """

from flask import jsonify
from . import app_views

@app_views.route('/status', methods=['GET'])
def get_status():
    """Returns status OK"""
    return jsonify({"status": "OK"})

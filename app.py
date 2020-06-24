# ---------------------------------------------------------
# Imports
# ---------------------------------------------------------

import click
import json
import os
import unittest
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from .database.models import Actor, Movie, setup_db
from .auth.auth import *

# ---------------------------------------------------------
# Config
# ---------------------------------------------------------


def create_app(test_config=None):
  # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers 
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response


    # GET all Actors
    @app.route('/actors', methods=['GET'])
    def get_actors():
        actors = Actor.query.all()

        if not actors:
            abort(404)

        return jsonify({
            'success': True,
            'actors': [actor.format() for actor in actors]
        }), 200

    

    # Error Handling
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(400)
    def resource_not_found(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app

app = create_app()
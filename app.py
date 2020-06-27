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
ROWS_PER_PAGE = 10


def paginate_results(request, selection):
        page = request.args.get('page', 1, type=int)
        start =  (page - 1) * ROWS_PER_PAGE
        end = start + ROWS_PER_PAGE
        objects_formatted = [object_name.format() for object_name in selection]
        return objects_formatted[start:end]

def create_app(test_config=None):
  # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers 
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def welcome():
        msg = 'Welcome to the Casting Agency'
        return jsonify(msg)

    # GET all Actors
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        actors = Actor.query.all()
        if not actors:
            abort(404)
        actors_paginated = paginate_results(request, actors)
        return jsonify({
            'success': True,
            'actors': actors_paginated
        }), 200

    # GET all movies
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        movies = Movie.query.all()
        if not movies:
            abort(404)
        movies_paginated = paginate_results(request, movies)
        return jsonify({
            'success': True,
            'movies': movies_paginated
        }), 200
    
    # Add new Actor record
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor(payload):
        body = request.get_json()
        if body is None:
            abort(400)
        name = body.get('name') or None
        age = body.get('age') or None
        gender = body.get('gender') or None
        if ((name is None) or (age is None) or (gender is None)):
            abort(400)
        actor = Actor(name=name, age=age, gender=gender)
        try:
            actor.insert()
        except Exception as e:
            abort(422)
        return jsonify({
            'success': True,
            'actor': actor.format()
        }), 200

    # Add new Movie record
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie(payload):
        body = request.get_json()
        if body is None:
            abort(400)
        title = body.get('title') or None
        release = body.get('release') or None
        if ((title is None) or (release is None)):
            abort(400)
        movie = Movie(title=title, release=release)
        try:
            movie.insert()
        except Exception as e:
            abort(422)
        return jsonify({
            'success': True,
            'actor': movie.format()
        }), 200

    # Update an actor record
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload, actor_id):
        if not actor_id:
            abort(404)
        actor = Actor.query.get(actor_id)
        if not actor:
            abort(404)
        body = request.get_json()
        if body is None:
            abort(400)
        if 'name' in body and body['name']:
            actor.name = body['name']
        if 'age' in body and body['age']:
            actor.age = body['age']
        if 'gender' in body and body['gender']:
            actor.gender = body['gender']
        actor.update()
        return jsonify({
            'success': True,
            'actor': actor.format(),
        }), 200

    # Update a movie record
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload, movie_id):
        if not movie_id:
            abort(404)
        movie = Movie.query.get(movie_id)
        if not movie:
            abort(404)
        body = request.get_json()
        if 'title' in body and body['title']:
            movie.title = body['title']
        if 'release' in body and body['release']:
            movie.release = body['release']
        movie.update()
        return jsonify({
            'success': True,
            'movie': movie.format(),
        }), 200

    # DELETE actor record
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):
        if not actor_id:
            abort(404)
        actor = Actor.query.get(actor_id)
        if not actor:
            abort(404)
        actor.delete()
        return jsonify({
            'success': True,
            'actor_id': actor_id
        }), 200

    # DELETE movie record
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, movie_id):
        if not movie_id:
            abort(404)
        movie = Movie.query.get(movie_id)
        if not movie:
            abort(404)
        movie.delete()
        return jsonify({
            'success': True,
            'movie_id': movie_id
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
    def bad_request(error):
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
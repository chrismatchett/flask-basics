import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flask import Flask, render_template, Response, request, redirect, url_for, json

bp = Blueprint('users', __name__)
users = []

@bp.route('/')
def index():
    # jumbotron.html is empty, get a template from Bootstrap Examples
    return render_template('jumbotron.html')

@bp.route('/hello/<name>')
def hello(name=None):
    # fix hello.html so that it says "Hello Chris" when you go to the URL on the next line
    # http://127.0.0.1:5000/hello?name=Chris 
    return render_template('hello.html')

@bp.route("/json/local")
def json_local():
    json_users = bp.open_resource('static/users.json')

    # open the file static/users.json
    # with json_users as ...
    # convert the data from json to python using json.load()
    # pass the data to render_template()

    return render_template('json_local.html')

@bp.route('/json/users', methods=['GET'])
def json_users():

    # add a global variable for our existing user list
    # if there are no users then show the users from static/users.json
    # pass the user data to render_template

    return render_template('json_users.html')

@bp.route('/json/users/add', methods=['POST'])
def json_add():
    
    # add a global variable for our existing user list
    # append the name sent from the json/users form to the list in json format
    # use the static/users.json as a reference to understand the format
    # redirect to json_users to show the updated user list

    return redirect(url_for('users.json_users')) 


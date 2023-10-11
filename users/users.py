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

@bp.route('/hello/<username>')
def hello(username=None):
    # fix hello.html so that it says "Hello Chris" when you go to the URL on the next line
    return render_template('hello.html', uname=username)

@bp.route("/json/local")
def json_local():
    json_users = bp.open_resource('static/users.json')
    
    # open the file static/users.json
    # with json_users as ...
    # convert the data from json to python using json.load()
    # pass the data to render_template()

    with json_users as f:
        local_users = json.load(f)

    return render_template('json_local.html', users=local_users)

@bp.route('/json/users', methods=['GET'])
def json_users():

    # add a global variable for our existing user list
    # if there are no users then show the users from static/users.json
    # pass the user data to render_template

    global users
    json_users = bp.open_resource('static/users.json')

    if len(users) == 0:
        with json_users as f:
            users = json.load(f)

    return render_template('json_users.html', users=users)

@bp.route('/json/users/add', methods=['POST'])
def json_add():
    
    # add a global variable for our existing user list
    # append the name sent from the json/users form to the list in json format
    # {"name": request.form.get('name')}
    # redirect to json_users to show the updated user list

    global users
    users.append({"name": request.form.get('name')})
    return redirect(url_for('users.json_users')) 


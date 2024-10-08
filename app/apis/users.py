#!/home/miyablo/.pyenv/versions/3.7.0/bin/python
# -*- coding: utf-8 -*-
from flask import request, Blueprint
from repository.users_repository import UsersRepository
from apis.utils import create_response, set_data_and_create_response

users_module = Blueprint("users", __name__)

@users_module.route('/signup', methods=['POST'])
def signup():
    try:
        if request.get_json()["user"]["email"] == "" or request.get_json()["user"]["password"] == "":
            raise Exception("email or password must not be empty")
        posted_user = request.get_json()["user"]
        user_id = UsersRepository().create(posted_user)
    except Exception as e:
        return(set_data_and_create_response("500", str(e)))

    response_data = {}
    response_data["message"] = 'successfully signed up'
    response_data["status"] = "200"
    response_data['data'] = { "user_id": user_id }
    
    return(create_response(response_data))


@users_module.route('/login', methods=['POST'])
def login():
    try:
        posted_user = request.get_json()["user"]
        is_success =  UsersRepository().check_login(posted_user["email"], posted_user["password"])
        if is_success:
            user_id = UsersRepository().fetch_user_id_by_email(posted_user["email"])
        else:
            raise Exception("email or password is wrong")
    except Exception as e:
        return(set_data_and_create_response("500", str(e)))

    response_data = {}
    response_data["message"] = 'successfully logged in'
    response_data["status"] = "200"
    response_data['data'] = { "user_id": user_id }
    
    return(create_response(response_data))

@users_module.route('/user/<string:user_id>', methods=['PATCH'])
def update(user_id):
    try:
        posted_user = request.get_json()["user"]
        UsersRepository().update(user_id, posted_user)
    except Exception as e:
        return(set_data_and_create_response("500", str(e)))

    response_data = {}
    response_data["message"] = 'successfully updated'
    response_data["status"] = "200"
    
    return(create_response(response_data))

@users_module.route('/user/<string:user_id>', methods=['GET'])
def show(user_id):
    try:
        user_info =  UsersRepository().show(user_id)
    except Exception as e:
        return(set_data_and_create_response("500", str(e)))

    response_data = {}
    response_data["message"] = 'success'
    response_data["status"] = "200"
    response_data["data"] = user_info
    
    return(create_response(response_data))
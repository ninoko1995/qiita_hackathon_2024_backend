#!/home/miyablo/.pyenv/versions/3.7.0/bin/python
# -*- coding: utf-8 -*-
from flask import request, Blueprint
from repository.spaces_repository import SpacesRepository
from apis.utils import create_response, set_data_and_create_response

spaces_module = Blueprint("spaces", __name__)


@spaces_module.route('/spaces', methods=['GET'])
def get_spaces():
    try:
        spaces =  SpacesRepository().index()
        for space in spaces:
            space["users"] = SpacesRepository().fetch_space_users(space["id"])
    except Exception as e:
        return(set_data_and_create_response("500", str(e)))

    response_data = {}
    response_data["message"] = 'success'
    response_data["status"] = "200"
    response_data["data"] = spaces
    
    return(create_response(response_data))


@spaces_module.route('/space/<string:space_id>', methods=['GET'])
def get_space(space_id):
    try:
        users_in_space =  SpacesRepository().fetch_space_users(space_id)
    except Exception as e:
        return(set_data_and_create_response("500", str(e)))

    response_data = {}
    response_data["message"] = 'success'
    response_data["status"] = "200"
    response_data["data"] = users_in_space
    
    return(create_response(response_data))


@spaces_module.route('/space/<string:space_id>/user/<string:user_id>', methods=['POST'])
def enter_space(space_id, user_id):
    try:
        position = request.get_json()["position"]
        SpacesRepository().create_space_users(space_id, user_id, position)
    except Exception:
        return(set_data_and_create_response("500"))

    response_data = {}
    response_data["message"] = 'successfully entered the space'
    response_data["status"] = "200"
    
    return(create_response(response_data))


@spaces_module.route('/space/<string:space_id>/user/<string:user_id>', methods=['PATCH'])
def update_user_status(space_id, user_id):
    try:
        status = request.get_json()["status"]
        SpacesRepository().update_space_users_status(space_id, user_id, status)
    except Exception:
        return(set_data_and_create_response("500"))

    response_data = {}
    response_data["message"] = "successfully update the user's status"
    response_data["status"] = "200"
    
    return(create_response(response_data))


@spaces_module.route('/space/<string:space_id>/user/<string:user_id>', methods=['DELETE'])
def leave_spave(space_id, user_id):
    try:
        SpacesRepository().delete_space_users(space_id, user_id)
    except Exception:
        return(set_data_and_create_response("500"))

    response_data = {}
    response_data["message"] = 'successfully left the space'
    response_data["status"] = "200"
    
    return(create_response(response_data))

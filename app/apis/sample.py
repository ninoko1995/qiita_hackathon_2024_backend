#!/home/miyablo/.pyenv/versions/3.7.0/bin/python
# -*- coding: utf-8 -*-
from flask import request, Blueprint
from repository.sample_repository import SampleRepository
from apis.utils import create_response, set_data_and_create_response

sample_module = Blueprint("sample", __name__)


@sample_module.route('/samples', methods=['GET'])
def get_samples():
    try:
        samples =  SampleRepository().fetch()
    except Exception as e:
        return(set_data_and_create_response("500", str(e)))

    response_data = {}
    response_data["message"] = 'success'
    response_data["status"] = "200"
    response_data["data"] = samples
    
    return(create_response(response_data))


@sample_module.route('/sample', methods=['POST'])
def create_sample():
    try:
        requested_report = request.get_json()["report"]
        SampleRepository().create(requested_report)
        samples = SampleRepository().fetch()
    except Exception:
        return(set_data_and_create_response("500"))

    response_data = {}
    response_data["message"] = 'success'
    response_data["status"] = "200"
    response_data["data"] = samples
    
    return(create_response(response_data))

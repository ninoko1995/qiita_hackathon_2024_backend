#!/home/miyablo/.pyenv/versions/3.7.0/bin/python
# -*- coding: utf-8 -*-
from flask import make_response
import json
from datetime import datetime, date, timedelta

# datetime型のデータをjson化するための処理
# ちなみにデータベースには、jst基準の時間が格納されている
def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, timedelta):
        return str(obj)
    raise TypeError("Type %s not serializable" % type(obj))


# JsonでかつUTF-8の文字コードで、レスポンスを返す
def create_response(response_data):
    response = make_response(json.dumps(response_data, default=json_serial, ensure_ascii=False))
    response.headers.add('Content-Type', 'application/json; charset=UTF-8')
    return response


def set_data_and_create_response(status, message="", data=""):
    response_data = {}
    response_data["status"] = status
    if message == "":
        if status=="500":
            response_data["message"] = "Internal Server Error"
        if status=="404":
            response_data["message"] = "Not Found"
        if status=="400":
            response_data["message"] = "Posted Data is wrong"
        if status=="200":
            response_data["message"] = "Success"
    else:
        response_data["message"] = message
    if data is not "":
        response_data["data"] = data
    return create_response(response_data)

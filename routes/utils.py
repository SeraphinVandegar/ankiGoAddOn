import json

from flask import abort

from domain.User import User


def getUserFromHeader(_request) -> User:
    try:
        auth_header = _request.headers.get('Authorization').replace("Bearer ", "")
        credentials = json.loads(auth_header)
        return User(credentials["username"], credentials["password"])
    except Exception as error:
        print(error)
        abort(401, description="Access Denied")
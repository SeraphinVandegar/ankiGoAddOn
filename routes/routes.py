import json

from User import User

from flask import request, jsonify, abort


def initRoutes(app):
    def getUserFromHeader(_request):
        try:
            auth_header = _request.headers.get('Authorization')
            credentials = json.loads(auth_header)
            return User(credentials["username"], credentials["password"])
        except Exception as error:
            print(error)
            abort(401, description="Access Denied")

    @app.route('/get-notes', methods=['GET'])
    def get_notes():
        user = getUserFromHeader(request)
        response = {
            "notes": user.getNotes()
        }
        return jsonify(response)

    @app.route('/get-notes-to-revise', methods=['GET'])
    def get_notes_to_revise():
        user = getUserFromHeader(request)
        ids = []
        for card in user.getCardsToRevise():
            ids.append(card.id)
        response = {
            "ids": ids
        }
        return jsonify(response)
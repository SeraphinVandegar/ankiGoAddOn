import json

from data.CardDto import CardDto
from data.User import User

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
        cards = []
        for c in user.getNotes():
            fields = c[6].split("\x1f")
            dto = CardDto(c[0], fields[0], fields[1], [x for x in c[5].split(" ") if x])
            cards.append(dto.toJson())
        return jsonify(cards)

    @app.route('/get-notes-to-revise', methods=['GET'])
    def get_notes_to_revise():
        user = getUserFromHeader(request)
        return jsonify([card.id for card in user.getCardsToRevise()])

    @app.route('/notes', methods=['POST'])
    def post_notes():
        data = request.json
        user = getUserFromHeader(request)
        user.createNote([data["front"], data["back"]])
        user.sync()
        return ""

    @app.route('/notes', methods=['DELETE'])
    def delete_notes():
        user = getUserFromHeader(request)
        id = request.args.get('id')
        user.deleteNote(id)
        user.sync()
        return ""
import json
import time

from data.CardDto import CardDto
from data.User import User

from flask import request, jsonify, abort


def initRoutes(app):
    def getUserFromHeader(_request) -> User:
        try:
            auth_header = _request.headers.get('Authorization')
            credentials = json.loads(auth_header)
            return User(credentials["username"], credentials["password"])
        except Exception as error:
            print(error)
            abort(401, description="Access Denied")

    @DeprecationWarning
    @app.route('/get-notes', methods=['GET'])
    def get_notes():
        user = getUserFromHeader(request)
        cards = []
        for c in user.getNotes():
            fields = c[6].split("\x1f")
            dto = CardDto(c[0], fields[0], fields[1], [x for x in c[5].split(" ") if x])
            cards.append(dto.toJson())
        return jsonify(cards)

    @app.route('/get-cards', methods=['GET'])
    def get_cards():
        user = getUserFromHeader(request)
        cards = []
        for c in user.getCardIds():
            fields = user.getCardFieds(c)
            if fields is None:
                print(f"unexpected: {c} has no field")
                continue
            dto = CardDto(c, fields[0], fields[1])
            cards.append(dto.toJson())
        return jsonify(cards)

    @app.route('/get-cards-to-revise', methods=['GET'])
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

    @app.route('/notes-revise', methods=['POST'])
    def revise_card():
        #Getting data
        user = getUserFromHeader(request)
        nid = int(request.args.get('id'))
        ease = int(request.args.get('ease'))
        startingTime = float(request.args.get('starting-time'))

        #Buiding the card to answer
        cid = ""
        for c in user.getCards():
            if nid == c.nid:
                cid = c.id
        card = user.getCard(cid)
        card.timer_started = startingTime

        #Answering the card and sync modifications
        user.answerCard(card, ease)
        user.sync()
        return ""
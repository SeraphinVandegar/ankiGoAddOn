import time

from flask import request

from domain.CardDto import CardDto
from routes.utils import getUserFromHeader
from services.userServices import UserServices

CARDS_ENDPOINT = '/cards'
CARDS_TO_REVISE_ENDPOINT = '/cards-to-revise'


def initUserRoutes(app):
    @app.route(CARDS_ENDPOINT, methods=['GET'])
    def getCards():
        return UserServices.getCards(getUserFromHeader(request))

    @app.route(CARDS_ENDPOINT, methods=['POST'])
    def createCard():
        data = request.json
        dtos = [CardDto(-1, dto['native'], dto['foreign'], dto['tags']) for dto in data]
        UserServices.createCard(getUserFromHeader(request), dtos)
        return ""

    @app.route(CARDS_ENDPOINT, methods=['PUT'])
    def updateCard():
        data = request.json
        dtos = [CardDto(int(dto['id']), dto['native'], dto['foreign'], dto['tags']) for dto in data]
        UserServices.updateNotes(getUserFromHeader(request), dtos)
        return ""

    @app.route(CARDS_TO_REVISE_ENDPOINT, methods=['GET'])
    def getCardsToRevise():
        return UserServices.getCardsToRevise(getUserFromHeader(request))

    @app.route(CARDS_TO_REVISE_ENDPOINT, methods=['PATCH'])
    def registerRevision():
        timer_started = time.time() - float(request.args.get('time_to_answer'))
        id = int(request.args.get('id'))
        ease = int(request.args.get('ease'))
        UserServices.registerRevision(getUserFromHeader(request), id, ease, timer_started)
        return ""

    @app.route(CARDS_ENDPOINT, methods=['DELETE'])
    def deleteNotes():
        UserServices.deleteNotes(getUserFromHeader(request), request.json)
        return ""

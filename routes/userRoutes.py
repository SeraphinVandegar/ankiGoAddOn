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
        dto = CardDto(-1, data['native'], data['foreign'], data['tags'])
        UserServices.createCard(getUserFromHeader(request), dto)
        return ""
    @app.route(CARDS_ENDPOINT, methods=['PUT'])
    def updateCard():
        pass

    @app.route(CARDS_TO_REVISE_ENDPOINT, methods=['GET'])
    def getCardsToRevise():
        pass

    @app.route(CARDS_TO_REVISE_ENDPOINT, methods=['PATCH'])
    def registerRevision():
        pass

    @app.route('/notes', methods=['DELETE'])
    def deleteNote():
        pass


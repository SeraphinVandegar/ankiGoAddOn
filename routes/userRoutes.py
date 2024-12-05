import json
import time
from multiprocessing import Lock

from flask import request

from domain.CardDto import CardDto
from routes.utils import getUserFromHeader
from services.userServices import UserServices

CARDS_ENDPOINT = '/cards'
CARDS_TO_REVISE_ENDPOINT = '/cards-to-revise'

user_locks = {
}


def getUserLock(_request):
    auth_header = request.headers.get('Authorization').replace("Bearer ", "")
    username = json.loads(auth_header)["username"]
    lock = user_locks.get(username)
    if lock is None:
        user_locks[username] = Lock()
    lock = user_locks.get(username)
    return lock


def initUserRoutes(app):
    @app.route(CARDS_ENDPOINT, methods=['GET'])
    def getCards():
        with getUserLock(request):
            return UserServices.getCards(getUserFromHeader(request))

    @app.route(CARDS_ENDPOINT, methods=['POST'])
    def createCard():
        with getUserLock(request):
            data = request.json
            dtos = [CardDto(-1, dto['native'], dto['foreign'], dto['tags']) for dto in data]
            UserServices.createCard(getUserFromHeader(request), dtos)
            return ""

    @app.route(CARDS_ENDPOINT, methods=['PUT'])
    def updateCard():
        with getUserLock(request):
            try:
                data = request.json
                dtos = [CardDto(int(dto['id']), dto['native'], dto['foreign'], dto['tags']) for dto in data]
                UserServices.updateNotes(getUserFromHeader(request), dtos)
            except:
                pass
            return ""

    @app.route(CARDS_TO_REVISE_ENDPOINT, methods=['GET'])
    def getCardsToRevise():
        with getUserLock(request):
            return UserServices.getCardsToRevise(getUserFromHeader(request))

    @app.route(CARDS_TO_REVISE_ENDPOINT, methods=['PATCH'])
    def registerRevision():
        with getUserLock(request):
            timer_started = time.time() - float(request.args.get('time_to_answer'))
            id = int(request.args.get('id'))
            ease = int(request.args.get('ease'))
            UserServices.registerRevision(getUserFromHeader(request), id, ease, timer_started)
            return ""

    @app.route(CARDS_ENDPOINT, methods=['DELETE'])
    def deleteNotes():
        with getUserLock(request):
            UserServices.deleteNotes(getUserFromHeader(request), request.json)
            return ""

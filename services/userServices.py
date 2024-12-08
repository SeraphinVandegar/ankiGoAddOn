from domain.CardDto import CardDto
from domain.User import User


class UserServices:

    @classmethod
    def getCards(cls, user: User) -> [CardDto]:
        dtos = []
        for card in user.getCards():
            fields = user.getCardFieldsFromCard(card)
            if fields is None:
                continue
            dtos.append(CardDto(card.id, fields[0], fields[1]).__dict__)
        return dtos

    @classmethod
    def createCard(cls, user: User, cardDto: [CardDto]):
        for cardDto in cardDto:
            user.createNote([cardDto.native, cardDto.foreign], cardDto.tags)
        user.sync()

    @classmethod
    def getCardsToRevise(cls, user: User):
        dtos = []
        for card in user.getCardsToRevise():
            fields = user.getCardFieldsFromCard(card)
            if fields is None:
                continue
            dtos.append(CardDto(card.id, fields[0], fields[1]).__dict__)
        return dtos

    @classmethod
    def registerRevision(cls, user: User, id: int, ease: int, timer_started: float):
        card = user.getCard(id)
        card.start_timer()
        card.timer_started = timer_started
        user.answerCard(card, ease)
        user.sync()

    @classmethod
    def deleteNotes(cls, user: User, ids: [int]):
        nids = []
        for id in ids:
            try:
               nids.append(user.getCard(int(id)).nid)
            except Exception as e:
                print(e)
                pass
        user.deleteNote(nids)
        user.sync()

    @classmethod
    def updateNotes(cls, user : User, cards : [CardDto]):
        for card in cards:
            nid = user.getCard(card.id).nid
            user.updateNote(nid, [card.native, card.foreign])
        user.sync()

import re
from domain.CardDto import CardDto
from domain.User import User

nextDuePattern = r"(review|learning).+?(?P<nextdue>scheduled_(secs|days): \d+)"


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
            user.createNote([cardDto.native, cardDto.foreign], cardDto.tags, "Plaint")
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
    def updateNotes(cls, user: User, cards: [CardDto]):
        for card in cards:
            nid = user.getCard(card.id).nid
            user.updateNote(nid, [card.native, card.foreign])
        user.sync()

    @classmethod
    def get_next_due_after_answer(cls, user, card_id):
        states = user.getSchedulingStates(card_id)
        return {
            "again": re.search(nextDuePattern, states.again.__str__(), flags=re.DOTALL).group("nextdue"),
            "hard": re.search(nextDuePattern, states.hard.__str__(), flags=re.DOTALL).group("nextdue"),
            "good": re.search(nextDuePattern, states.good.__str__(), flags=re.DOTALL).group("nextdue"),
            "easy": re.search(nextDuePattern, states.easy.__str__(), flags=re.DOTALL).group("nextdue"),
        }

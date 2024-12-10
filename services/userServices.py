import re
from domain.User import User

nextDuePattern = r"(review|learning).+?(?P<nextdue>scheduled_(secs|days): \d+)"


class UserServices:

    @classmethod
    def getCards(cls, user: User) -> [dict]:
        dtos = []
        for card in user.getCards():
            card = cls.mapToUsableCard(user, card)
            dtos.append(card)
        return dtos

    @classmethod
    def createCard(cls, user: User, cardDtos: [dict]):
        for cardDto in cardDtos:
            user.createNote([cardDto["question"], cardDto["answer"]], note_type_name="Plaint")
        user.sync()

    @classmethod
    def getCardsToRevise(cls, user: User):
        dtos = []
        for card in user.getCardsToRevise():
            card = cls.mapToUsableCard(user, card)
            dtos.append(card)
            #fields = user.getCardFieldsFromCard(card)
            #if fields is None:
            #    continue
            #dtos.append(CardDto(card.id, fields[0], fields[1]).__dict__)
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
    def updateNotes(cls, user: User, cards: [dict]):
        for card in cards:
            user.updateNote(card["nid"], [card["question"], card["answer"]])
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

    @classmethod
    def mapToUsableCard(cls, user, card):
        pattern = r"__\$\$(?P<field>.*)__\$\$"
        return {
            "id": card.id,
            "nid": card.nid,
            "question": re.search(pattern, card.question(), flags=re.DOTALL).group("field"),
            "answer": re.search(pattern, card.answer(), flags=re.DOTALL).group("field"),
            "next_due": UserServices.get_next_due_after_answer(user, card.id)
        }
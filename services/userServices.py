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
    def createCard(cls, user: User, cardDto : [CardDto]):
        for cardDto in cardDto:
            user.createNote([cardDto.native, cardDto.foreign], cardDto.tags)
        user.sync()
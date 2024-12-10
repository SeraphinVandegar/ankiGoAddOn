from domain.User import User

from services.userServices import UserServices

user = User("s.vandegar@student.helmo.be", "_")

for card in user.getCards():
    print(UserServices.getCurrentState(user, card.id))

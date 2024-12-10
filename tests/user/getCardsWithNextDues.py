import re
from domain.User import User
from services.userServices import UserServices

user = User("s.vandegar@student.helmo.be", "_")

for card in user.getCards():
    print(UserServices.get_next_due_after_answer(user, card.id))

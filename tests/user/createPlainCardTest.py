from domain.User import User

import re

from services.userServices import UserServices

user = User("s.vandegar@student.helmo.be", "_")
user.createNote(["Capitale de France", "Now"], note_type_name="Plaint")

for card in user.getCards():
    print(UserServices.mapToUsableCard(user, card))

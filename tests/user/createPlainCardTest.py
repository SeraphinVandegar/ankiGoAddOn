from domain.User import User

import re

from services.userServices import UserServices

user = User("s.vandegar@student.helmo.be", "pppppppp")
user.createNote(["Capitale de France", "Paris\nOu Berlin"], note_type_name="Plaint")

for card in user.getCards():
    print(UserServices.mapToUsableCard(user, card))

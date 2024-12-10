from domain.User import User

import re

from services.userServices import UserServices

user = User("s.vandegar@student.helmo.be", "pppppppp")
user.createNote(["Capitale de France", "Paris\nOu Berlin"], note_type_name="Plaint")

pattern = r"__\$\$(?P<field>.*)__\$\$"
def getUsableCard(card):
    return {
        "id": card.id,
        "nid": card.nid,
        "question": re.search(pattern, card.question(), flags=re.DOTALL).group("field"),
        "answer": re.search(pattern, card.answer(), flags=re.DOTALL).group("field"),
        "next_due": UserServices.get_next_due_after_answer(user, card.id)
    }
for card in user.getCards():
    print(getUsableCard(card))

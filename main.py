from User import User

helmo = User("s.vandegar@student.helmo.be", "pppppppp")
#howest = User("seraphin.vandegar@student.howest.be", "pppppppp")

card = helmo.getCardsToRevise()[0]
card.start_timer()


fields = helmo.getCardFields(card._to_backend_card().note_id)
print(fields)

fields = helmo.getCardFieldsFromCard(card)
print(fields)
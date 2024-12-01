from User import User

helmo = User("s.vandegar@student.helmo.be", "pppppppp")
#howest = User("seraphin.vandegar@student.howest.be", "pppppppp")

print(len(helmo.getCardsToRevise()))
card = helmo.getCardsToRevise()[0]
card.start_timer()
#card = Card(helmo.col, _card.id ,backend_card=_card)
card.start_timer()
print(type(card))
print(card)
print(helmo.answerCard(card, 3))
print(len(helmo.getCardsToRevise()))

helmo.sync()
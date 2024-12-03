import time

from domain.User import User

user = User("s.vandegar@student.helmo.be", "_")

c = user.getCardsToRevise()[0]
c.timer_started = time.time()
print(c.__dict__)
user.answerCard(c, 1)

c2 = user.getNotes()[0]

print(user.getCard(user.getCardIds()[0]).__dict__)
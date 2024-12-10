import time

from domain.User import User

user = User("s.vandegar@student.helmo.be", "_")

c = user.getCardsToRevise()[0]
c.timer_started = time.time()
print(c.__dict__)
user.answerCard(c, 1)

c2 = user.getNotes()[0]

print(user.getCard(user.getCardIds()[0]).__dict__)



sched = user.col.sched

card = sched.getCard()

again_interval = sched.nextIvl(card, ease=1)
print(again_interval)
again_interval = sched.nextIvl(card, ease=2)
print(again_interval)
again_interval = sched.nextIvl(card, ease=3)
print(again_interval)
again_interval = sched.nextIvl(card, ease=4)
print(again_interval)


states = user.col._backend.get_scheduling_states(card.id)
print(states.again)
print(states.hard)
print(states.good)
print(states.easy)
print(states.current)

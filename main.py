from User import User

helmo = User("s.vandegar@student.helmo.be", "pppppppp")
#print(helmo.get_due_counts())
howest = User("seraphin.vandegar@student.howest.be", "pppppppp")

c = helmo.get_due_counts()
print("__ C __")
print(c)
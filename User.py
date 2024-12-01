from anki.collection import Collection

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.col = Collection(f"/Users/seraphin/Library/Application Support/Anki2/{username}/collection.anki2")

    def getNotes(self):
        return self.col.db.all("SELECT * FROM notes")

    def createCard(self):
        note = self.col.newNote()
        note.fields = ["Sera", "Fofole"]
        note.tags = ["Paris", "Geography"]
        note.deck = "Defaxult"
        print(note.deck)
        self.col.addNote(note)

    def sync(self):
        auth = self.col.sync_login(self.username, self.password, None)
        self.col.sync_collection(auth, False)

    def deleteNotes(self):
        self.col.db.all("DELETE FROM notes")


    def getCardsToRevise(self):
        sched = self.col.sched

        # Get counts of cards to revise
        due_counts = sched.get_queued_cards(fetch_limit=1000)
        return due_counts

    def get_due_card(self):
        return self.col.sched.getCard()

    def answerCard(self, card, ease):
        self.col.sched.answerCard(card, ease)
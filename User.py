from anki.collection import Collection

from anki.cards import Card


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.col = Collection(f"/Users/seraphin/Library/Application Support/Anki2/{username}/collection.anki2")
        self.fieldsById = dict()
        self.refreshNotesMap()

    def refreshNotesMap(self):
        for note in self.getNotes():
            self.fieldsById[note[0]] = note[6].split("\x1f")

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
        due_counts = self.col.sched.get_queued_cards(fetch_limit=1000)
        return list(map(
            lambda backendCard: Card(self.col, backendCard.card.id, backend_card=backendCard.card), due_counts.cards))

    def getCardToRevise(self):
        return self.col.sched.getCard()

    def answerCard(self, card, ease):
        self.col.sched.answerCard(card, ease)

    def getCardFields(self, card: int):
        try:
            fields = self.fieldsById[card]
            return fields
        except:
            pass
        self.refreshNotesMap()
        try:
            fields = self.fieldsById[card]
            return fields
        except:
            pass
        return None

    def getCardFieldsFromCard(self, card: Card):
        return self.getCardFields(card._to_backend_card().note_id)

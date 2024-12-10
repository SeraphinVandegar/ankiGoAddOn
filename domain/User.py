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

    def createNote(self, fields, tags=None, note_type_name="Plaint"):
        if tags is None:
            tags = []

        model = self.col.models.byName(note_type_name)
        if not model:
            raise ValueError(f"Note type '{note_type_name}' does not exist.")
        note = self.col.newNote()
        note.fields = fields
        note.tags = tags
        self.col.addNote(note)
        return note

    def sync(self):
        auth = self.col.sync_login(self.username, self.password, None)
        self.col.sync_collection(auth, True)

    def deleteNote(self, ids: [int]):
        self.col.remove_notes(ids)

    def _deleteAllNotesAndCards(self):
        self.col.db.all("DELETE FROM notes")
        self.col.db.all("DELETE FROM cards")

    def getCardsToRevise(self):
        due_counts = self.col.sched.get_queued_cards(fetch_limit=1000)
        return list(map(
            lambda backendCard: Card(self.col, backendCard.card.id), due_counts.cards))

    def getCardIds(self):
        return self.col.find_cards("")

    def getCard(self, id):
        return Card(self.col, id)

    def getCardToRevise(self):
        return self.col.sched.getCard()

    def answerCard(self, card, ease):
        self.col.sched.answerCard(card, ease)

    def getCardFieds(self, card: id(int)):
        card = self.col.get_card(card)
        return self.getNoteFields(card.nid)

    def getNoteFields(self, id: int):
        try:
            fields = self.fieldsById[id]
            return fields
        except:
            pass
        self.refreshNotesMap()
        try:
            fields = self.fieldsById[id]
            return fields
        except:
            pass
        return None

    def getCardFieldsFromCard(self, card: Card):
        return self.getNoteFields(card._to_backend_card().note_id)

    def getCards(self) -> [Card]:
        cards = [self.col.get_card(id) for id in self.col.find_cards("")]
        return cards

    def updateNote(self, id, fields):
        note = self.col.get_note(id)
        note.fields = fields
        self.col.update_note(note)

    def getSchedulingStates(self, card_id):
        return self.col._backend.get_scheduling_states(card_id)

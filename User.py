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

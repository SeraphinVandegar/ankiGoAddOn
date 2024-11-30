from anki.collection import Collection

col = Collection("/Users/seraphin/Library/Application Support/Anki2/test/collection.anki2")


def saveSync():
    def sync_deck():
        auth = col.sync_login("seraphin.vandegar@student.howest.be", "pppppppp", None)
        #auth = col.sync_login("s.vandegar@student.helmo.be", "pppppppp", None)
        #auth = col.sync_login("sera.vandegar@gmail.com", "pppppppp", None)
        ##col.save(trx=False)
        col.sync_collection(auth, False)
    sync_deck()

def getNotes():
    notes = col.db.all("SELECT * FROM notes WHERE tags LIKE ?", "%Paris%") #% .* in regex

    # Loop through and print details of each note
    for note in notes:
        print(note)

def createCard():
    # Get the model (note type) by name
    model = col.models.byName("Basic")

    print(model)

    # Get the deck by name
 #   deck = col.decks.byName("Default")
 #   print(deck)

    # Create a new note
    note = col.newNote()

    print(note)
    print(note.fields)

    fields = ["Magali", "Fofole"]
    # Set the fields (content) of the note
    for i, field in enumerate(fields):
        note.fields[i] = field

    print(note.fields)
    note.tags = ["Paris", "Geography"]
    col.addNote(note)
    """
    # Set the tags for the note
    
    
    # Add the note to the collection (which also creates the card(s))
    col.addNote(note)"""

#getNotes()

createCard()
saveSync()

def deleteNotes():
    notes = col.db.all("DELETE FROM notes")

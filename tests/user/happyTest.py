from User import User


def checkNoteAdded(u, note):
    found = False
    for n in u.getNotes():
        if n[0] == note.id:
            found = True
            break
    if not found:
        raise Exception("Note not found")


def checkNoteDeleted(u, note):
    found = False
    for n in u.getNotes():
        if n[0] == note.id:
            found = True
            break
    if found:
        raise Exception("Note found")


user = User("s.vandegar@student.helmo.be", "_")

testingNote = user.createNote(["front", "back"])
checkNoteAdded(user, testingNote)
user.deleteNote(testingNote.id)
checkNoteDeleted(user, testingNote)

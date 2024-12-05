from domain.User import User


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


def checkCardFields(u, nid, fields):
    if not (u.getNoteFields(nid) == fields):
        raise Exception("Fields not equal")


user = User("s.vandegar@student.helmo.be", "_")

testingNote = user.createNote(["front", "back"])
checkNoteAdded(user, testingNote)
checkCardFields(user, testingNote.id, ["front", "back"])


testingNote2 = user.createNote(["front", "back"])
user.updateNote(testingNote2.id, ["front4", "back3"])
checkCardFields(user, testingNote2.id, ["front4", "back3"])

user.deleteNote([str(testingNote.id), str(testingNote2.id)])
checkNoteDeleted(user, testingNote)
checkNoteDeleted(user, testingNote2)


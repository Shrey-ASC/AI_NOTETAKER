from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

FILE = "notes.json"


# Create file if it doesn't exist
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)


# Read notes
def readnote():
    with open(FILE, "r") as f:
        return json.load(f)


# Write notes
def writenote(notes):
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=4)


# GET all notes
@app.route('/notes', methods=['GET'])
def getnotes():
    notes = readnote()
    return jsonify(notes)


# POST create new note
@app.route('/notes', methods=['POST'])
def addnote():
    notes = readnote()
    data = request.get_json()

    new_note = {
        "id": len(notes) + 1,
        "note": data.get("note")
    }

    notes.append(new_note)
    writenote(notes)

    return jsonify(new_note)


@app.route('/notes', methods=['PUT'])
def updatenote():
    notes = readnote()
    data = request.get_json()

    note_id = data.get("id")
    new_note = data.get("note")

    for note in notes:
        if note["id"] == note_id:
            note["note"] = new_note
            writenote(notes)
            return jsonify(note)

    return jsonify({"message": "Note not found"})

@app.route('/notes', methods=['DELETE'])
def deletenote():
    notes = readnote()
    data = request.get_json()

    note_id = data.get("id")

    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            writenote(notes)
            return jsonify({"message": "Note deleted"})

    return jsonify({"message": "Note not found"})
    

if __name__ == "__main__":
    app.run(debug=True)
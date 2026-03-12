
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

FILE = 'notes.json'


def readnote():
    with open(FILE, 'r') as f:
        return json.load(f)


def writenote(notes):
    with open(FILE, 'w') as f:
        json.dump(notes, f, indent=4)


# READ
@app.route('/notes', methods=['GET'])
def getnotes():
    notes = readnote()
    return jsonify(notes)


# CREATE
@app.route('/notes', methods=['POST'])
def addnote():
    notes = readnote()
    data = request.get_json()

    new_note = {
        "id": len(notes) + 1,
        "note": data["note"]
    }

    notes.append(new_note)
    writenote(notes)

    return jsonify(new_note)


# UPDATE
@app.route('/notes/<int:id>', methods=['PUT'])
def updatenote(id):
    notes = readnote()
    data = request.get_json()

    for note in notes:
        if note["id"] == id:
            note["note"] = data["note"]
            writenote(notes)
            return jsonify(note)

    return {"message": "Note not found"}


# DELETE
@app.route('/notes/<int:id>', methods=['DELETE'])
def deletenote(id):
    notes = readnote()

    for note in notes:
        if note["id"] == id:
            notes.remove(note)
            writenote(notes)
            return {"message": "Note deleted"}

    return {"message": "Note not found"}


if __name__ == '__main__':
    app.run(debug=True)
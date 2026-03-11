import flask from flask 
import request
import jsonify
import os
import json

app = Flask(__name__)

notes = [
    {"id": 1, "title": "Physics"},
    {"id": 2, "title": "Grammar"},
    {"id": 3, "title": "maths"}
]

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = next((note for note in notes if note["id"] == note_id), None)
    return jsonify(note) if note else (jsonify({"error": "Note not found"}), 404)

@app.route('/notes', methods=['POST'])
def add_note():
    new_note = request.json
    notes.append(new_note)
    return jsonify(new_note), 201

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    note = next((note for note in notes if note["id"] == note_id), None)
    if not note:
        return jsonify({"error": "Note not found"}), 404

    data = request.json
    note.update(data)
    return jsonify(note)

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    global notes
    notes = [note for note in notes if note["id"] != note_id]
    return jsonify({"message": "Note deleted"})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request

app = Flask(__name__)

# data
notes = [
    {"id": 1, "note": "API"},
    {"id": 2, "note": " DSA"}
]

# read
@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)


# create
@app.route('/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    new_note = {
        "id": len(notes) + 1,
        "note": data["note"]
    }
    notes.append(new_note)
    return jsonify(new_note)


# update
@app.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):
    data = request.get_json()
    
    for note in notes:
        if note["id"] == id:
            note["note"] = data["note"]
            return jsonify(note)

    return {"message": "Note not found"}


# delete
@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):

    for note in notes:
        if note["id"] == id:
            notes.remove(note)
            return {"message": "Note deleted"}

    return {"message": "Note not found"}


if __name__ == '__main__':
    app.run(debug=True)
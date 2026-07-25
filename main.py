from flask import Flask, request, jsonify
from models import db, Note

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///notes.db'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/api/notes', methods=['GET'])
def get_notes():
    notes = db.session.execute(db.select(Note)).scalars()
    notes_data = [note.to_dict() for note in notes]
    return jsonify(notes_data)

@app.route('/api/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    new_note = Note(title=data.get("title"), content=data.get("content"))
    db.session.add(new_note)
    db.session.commit()
    return jsonify(new_note.to_dict()), 201

if __name__ == "__main__":
    app.run(debug=True, port=5001)
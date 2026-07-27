from flask import Flask, request, jsonify
import bcrypt
from models import db, Note, User
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///notes.db'
app.config["JWT_SECRET_KEY"] = 'asdfkj*A&*HA&@^O_'

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

@app.route('/api/notes', methods=['GET'])
@jwt_required()
def get_notes():
    user_id = get_jwt_identity()
    notes = db.session.execute(db.select(Note).where(Note.user_id == int(user_id))).scalars()
    notes_data = [note.to_dict() for note in notes]
    return jsonify(notes_data)

@app.route('/api/notes', methods=['POST'])
@jwt_required()
def add_note():
    data = request.get_json()
    user_id = get_jwt_identity()
    new_note = Note(title=data.get("title"), content=data.get("content"), user_id=int(user_id))
    db.session.add(new_note)
    db.session.commit()
    return jsonify(new_note.to_dict()), 201

@app.route('/api/notes/<int:note_id>', methods=['PUT'])
@jwt_required()
def update_note(note_id):
    note = db.session.get(Note, note_id)
    user_id = int(get_jwt_identity())

    if note:
        if note.user_id != user_id:
            return jsonify("error: bad credentials"), 401
        
        updated_content = request.get_json()
        note.title = updated_content.get("title", note.title)
        note.content = updated_content.get("content", note.content)
        db.session.commit()

        return jsonify(note.to_dict()), 200

    return jsonify("Error: resource not found"), 404

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
@jwt_required()
def delete_note(note_id):
    note = db.session.get(Note, note_id)
    user_id = int(get_jwt_identity())

    if note:
        if note.user_id != user_id:
            return jsonify("error: bad credentials"), 401
        
        db.session.delete(note)
        db.session.commit()
        return "", 204
    
    return jsonify("Error: resource not found"), 404

@app.route('/api/register', methods=['POST'])
def register():

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email and password:
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(email=email, password_hash=password_hash.decode('utf-8'))
        db.session.add(new_user)
        db.session.commit()
        return jsonify("Success: user created successfully"), 201
    
    return jsonify("error: register failed"), 400

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    
    user = db.session.execute(db.select(User).where(User.email == email)).scalar()
    if user:
        password = data.get('password').encode('utf-8')
        if bcrypt.checkpw(password, user.password_hash.encode('utf-8')):
            token = create_access_token(identity=str(user.id))

            return jsonify(access_token=token), 200

    return jsonify("Error: bad credentials"), 401

if __name__ == "__main__":
    app.run(debug=True, port=5001)
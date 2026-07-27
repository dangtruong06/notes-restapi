Notes API (REST + JWT basics)

A small full-stack notes project with REST API and JWT auth.

Stack
Backend: Flask, Flask-SQLAlchemy (SQLite), flask-jwt-extended, bcrypt
Frontend: React
Features
User registration and login with bcrypt-hashed passwords
JWT-based authentication
Full CRUD on notes: Create, Read, Update, Delete
Notes are scoped per-user — each user only sees their own notes
Ownership checks on update/delete — a user can't modify another user's notes
Setup
bash
python -m venv venv
source venv/bin/activate   # venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py

API Endpoints
Method	Route	Auth required	Description
POST	/api/register	No	Create a new user
POST	/api/login	No	Log in, returns a JWT access token
GET	/api/notes	Yes	List the logged-in user's notes
POST	/api/notes	Yes	Create a note
PUT	/api/notes/<id>	Yes	Update a note (must be the owner)
DELETE	/api/notes/<id>	Yes	Delete a note (must be the owner)

Protected routes require an Authorization: Bearer <token> header, using the token returned from /api/login.

Testing

Tested manually with Postman. Typical flow:

POST /api/register with {"email": ..., "password": ...}
POST /api/login with the same credentials → copy the access_token from the response
In Postman, set Authorization tab → Bearer Token → paste the token
Hit any /api/notes route with that token attached

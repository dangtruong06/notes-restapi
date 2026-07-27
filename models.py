from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class Note(db.Model):
    __tablename__ = "notes"

    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[String] = mapped_column(String(250))
    content:Mapped[Text] = mapped_column(Text)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "content":self.content}
    
class User(db.Model):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(primary_key=True)
    email:Mapped[String] = mapped_column(String(250), nullable=False, unique=True)
    password_hash:Mapped[String] = mapped_column(String(250), nullable=False)

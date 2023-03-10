from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Cats(db.Model):
    __tablename__ = "Cats"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        unique=True
    )
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Cat {self.id}, {self.name}>"
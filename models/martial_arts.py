from app import db

class MartialArts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(40), nullable=False)
    points = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


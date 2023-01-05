from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    owner= db.Column(db.String)
# one board can have many cards -> we have a one to many relationship which means our card model (child) 
# is going to get the foreign key from the board model (parent)
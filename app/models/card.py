from app import db
from flask import abort, make_response

# Child model
class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)
    # board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'))
    # board= db.relationship("Board", back_populates="cards")
    
    # converting the response from class instance to dict
    def to_dict(self):
        return {
            "id": self.card_id,
            "message": self.message,
            "likes_count": self.likes_count,
            "board_id": self.board_id
        }
    
    @classmethod 
    #instance methods are for classes that already exist (instances of class)
    # class methods are called on the class itself -> it turns the request from a dictionary to a class instance
    def from_dict(cls, request_body):
        return cls(
            # we omit id because or model autogenerates id-> line 5
            message= request_body["message"],
            likes_count= request_body["likes_count"],
            board_id= request_body["board_id"]
        )

    # checking that each post request has all input fields filled
    # def update(self, request_body):
    #     try:
    #         self.message=request_body["message"],
    #         self.likes_count= request_body["likes_count"]
    #     except KeyError as err:
    #         abort(make_response({"details":"missing attribute {err}"}))


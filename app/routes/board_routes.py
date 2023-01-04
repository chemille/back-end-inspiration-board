from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board

# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("board", __name__, url_prefix="/board")

# Create a New Board -> post method

@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    
    try:
        new_board = Board(
            # board_id=request_body["board_id"],
            title=request_body["title"],
            owner=request_body["owner"]
        )
    except KeyError:
        return {"details": "Missing Data"}, 400

    db.session.add(new_board)
    db.session.commit()

    return make_response(f"Board {new_board.title} has been successfully created", 201)
    # we also can send back the entire dictionary (new board) as confirmation to the client

    
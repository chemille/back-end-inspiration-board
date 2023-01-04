from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board

# example_bp = Blueprint('example_bp', __name__)
boards_bp = Blueprint("board", __name__, url_prefix="/boards")

# Create a New Board -> post method
@boards_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    
    try:
        new_board = Board(
            title=request_body["title"],
            owner=request_body["owner"]
        )
    except KeyError:
        return {"details": "Missing Data"}, 400

    db.session.add(new_board)
    db.session.commit()

    # return make_response(f"Board {new_board.title} has been successfully created", 201)
    # we also can send back the entire dictionary (new board) as confirmation to the client
    return {
        "board" : {
            "id": new_board.board_id,
            "title": new_board.title,
            "owner": new_board.owner
        }
    }, 201

# Get ALL Boards
@boards_bp.route("", methods=["GET"])
def read_all_boards():

    boards = Board.query.all()
    boards_response = []

    for board in boards:
        boards_response.append(
            {
            "id": board.board_id,
            "title": board.title,
            "owner": board.owner
            }
        )
    return jsonify(boards_response)


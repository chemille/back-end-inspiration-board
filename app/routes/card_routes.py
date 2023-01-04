from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.card import Card

cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

# Create a New Card
@cards_bp.route("", methods=["POST"])
def create_card():
    request_body = request.get_json()

    try:
        new_card = Card(
            message=request_body["message"],
            likes_count=request_body["likes_count"]
        )
    except KeyError:
        return {"details": "Missing Data"}, 400
    
    db.session.add(new_card)
    db.session.commit()

    return {
        "card" : {
            "id": new_card.card_id,
            "message": new_card.message,
            "likes_count": new_card.likes_count
        }
    }, 201
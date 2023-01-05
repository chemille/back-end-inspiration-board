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


# Get ALL cards
@cards_bp.route("", methods=["GET"])
def read_all_cards():

    cards = Card.query.all()
    cards_response = []

    for card in cards:
        cards_response.append(
            {
                "id": card.card_id,
                "message": card.message,
                "likes_count": card.likes_count
            }
        )
    return jsonify(cards_response)

# Validate Card helper function
def validate_card(card_id):
    try:
        card_id = int(card_id)
    except:
        abort(make_response({"details": "Invalid Data, id must be a number"}, 400))
    
    card = Card.query.get(card_id)
    print("card test print", card)
    if not card:
        abort(make_response({"details": f"There is no existing card {card_id}"}, 400))
    
    return card

# Get ONE Card
@cards_bp.route("/<card_id>", methods=["GET"])
def read_one_card(card_id):
    card = validate_card(card_id)

    return {
        "card": {
            "id": card.card_id,
            "messsage": card.message,
            "likes_count": card.likes_count
        }
    }


# Delete a card
@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    card = validate_card(card_id)

    db.session.delete(card)
    db.session.commit()

    # return {
    #     "details": f'card {card.title} owned by {card.owner} successfully deleted'
    # }
    return {
        "details": f'Card {card.card_id} successfully deleted'
    }

# Update likes
@cards_bp.route("/<card_id>/like", methods=["PUT"])
def update_likes(card_id):
    card = validate_card(card_id)

    request_body =request.get_json()
    card.likes_count = request_body["likes_count"]

    card.likes_count = int(card.likes_count) + 1
    # print("LIKE COUNT", card.likes_count)
    # print("TYPE", type(card.likes_count))

    db.session.commit()
    
    return {
        "card": {
            "id": card.card_id,
            "messsage": card.message,
            "likes_count": card.likes_count 
        }
    }

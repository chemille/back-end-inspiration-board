from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.card import Card
from app.routes.routes_helper import validate_model

cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

# Create a New Card
@cards_bp.route("", methods=["POST"])
def create_card():
    request_body = request.get_json()

    try:
        new_card = Card.from_dict(request_body)
        # new_card = Card(
        #     message=request_body["message"],
        #     likes_count=request_body["likes_count"],
        #     board_id=request_body["board_id"]
        # )
    except KeyError:
        return {"details": "Missing Data"}, 400


    db.session.add(new_card)
    db.session.commit()

    return jsonify(new_card.to_dict()), 201

    # return {
    #     "card" : {
    #         "id": new_card.card_id,
    #         "message": new_card.message,
    #         "likes_count": new_card.likes_count,
    #         "board_id": new_card.board_id
    #     }
    # }, 201


# Get ALL cards
@cards_bp.route("", methods=["GET"])
def read_all_cards():
    
    cards = Card.query.all()
    cards_response = [card.to_dict() for card in cards]

    # for card in cards:
    #     cards_response.append(
    #         {
    #             "id": card.card_id,
    #             "message": card.message,
    #             "likes_count": card.likes_count
    #         }
    #     )
    return jsonify(cards_response)


# Get ONE Card
@cards_bp.route("/<card_id>", methods=["GET"])
def read_one_card(card_id):
    card = validate_model(Card, card_id)
    # card = validate_card(card_id)

    return card.to_dict()
    # return {
    #     "card": {
    #         "id": card.card_id,
    #         "messsage": card.message,
    #         "likes_count": card.likes_count
    #     }
    # }


# Delete a card
@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    card = validate_model(Card, card_id)
    # card = validate_card(card_id)

    db.session.delete(card)
    db.session.commit()


    return {
        "details": f'Card {card.card_id} successfully deleted'
    }

# Update likes
@cards_bp.route("/<card_id>/likes", methods=["PUT"])
def update_likes(card_id):
    card = validate_model(Card, card_id)
    # card = validate_card(card_id)

    request_body =request.get_json()
    card.likes_count = request_body["likes_count"]

    card.likes_count = int(card.likes_count) + 1
    
    db.session.commit()
    
    return card.to_dict()
    # return {
    #     "card": {
    #         "id": card.card_id,
    #         "messsage": card.message,
    #         "likes_count": card.likes_count 
    #     }
    # }

from flask import make_response, abort

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{cls.__name__} {model_id} invalid, id must be a number"}, 400))
    
    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message": f"There is no existing {cls.__name__} {model_id}"}, 404))
    
    return model



    # # Validate board and validate card helper function
# def validate_card(card_id):
#     try:
#         card_id = int(card_id)
#     except:
#         abort(make_response({"details": "Invalid Data, id must be a number"}, 400))
    
#     card = Card.query.get(card_id)
#     print("card test print", card)
#     if not card:
#         abort(make_response({"details": f"There is no existing card {card_id}"}, 400))
    
#     return card
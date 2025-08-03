from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import db_helper
import generic_helper

app = FastAPI()

inprogress_orders = {}



@app.post("/")
async def handle_request(request:Request):
    payload = await request.json()
    
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    print("**********")
    print(output_contexts[0]['name'])
    session_id = generic_helper.extract_session_id(output_contexts[0]['name'])

    #intent_handler_dict = {
    #     'order_add' : add_to_order,
    #     'order_remove':remove_from_order,
    #     'order_complete':complete_order,
    #     'track_order_with_number':track_order
    # }

    if intent == "track_order_with_number":
        return track_order(parameters,session_id)
    elif intent == "order_complete":
        return complete_order(parameters,session_id)
    elif intent == "order_add":
        return add_to_order(parameters,session_id)
    elif intent == "order_remove":
        return remove_from_order(parameters,session_id)

def complete_order(parameters : dict,session_id):
    if session_id not in inprogress_orders:
        fulfillmentText = "There is some issue with you order. Please reorder !"
    else:
        order = inprogress_orders[session_id]
        order_id = save_to_db(order)
        order_total = db_helper.get_order_total(order_id)
        if order_id == -1:
            fulfillmentText = "There is some issue with you order. Please reorder !"
        else:
            order_str = generic_helper.get_str_from_food_dict(order)
            fulfillmentText = f"Your order has been placed with id : {order_id}. Your total bill is {order_total}. You order summary : {order_str}"
    del inprogress_orders[session_id]
    return JSONResponse(content={
        "fulfillmentText": fulfillmentText
    })

def save_to_db(order : dict):
    next_order_id = db_helper.get_next_order_id()
    for food_item,quantity in order.items():
        rcode = db_helper.insert_order_item(
            food_item,
            quantity,
            next_order_id
        )
        if rcode == -1:
            return -1
    db_helper.insert_order_tracking(next_order_id,"In Progress")
    return next_order_id



def remove_from_order(parameter : dict,session_id : str):
    if session_id not in inprogress_orders:
        fulfillmentText = "There is some issue. Pls try again later."
    else:
        removed_items = []
        not_removed_items = []
        current_order = inprogress_orders[session_id]
        food_items = parameter["food_item"]

        for item in food_items:
            if item not in current_order:
                not_removed_items.append(item)
            else:
                removed_items.append(item)
                del current_order[item]
        print(len(removed_items))
        print(len(not_removed_items))


        parts = []

        if len(removed_items) > 0:
            parts.append(f"Removed {', '.join(removed_items)} from your order.")
        if len(not_removed_items) > 0:
            parts.append(f"Your current order does not have {', '.join(not_removed_items)}.")

        if len(current_order.keys()) == 0:
            fulfillmentText = "Sorry, your order is empty."
        else:
            order_str = generic_helper.get_str_from_food_dict(current_order)
            # Always include the else-style summary regardless of earlier parts
            summary = f"Here is your updated order: {order_str}. Is there any item to be added?"
            if parts:
                fulfillmentText = " ".join(parts) + " " + summary
            else:
                fulfillmentText = summary

        return JSONResponse(content={
            "fulfillmentText": fulfillmentText
        })










def add_to_order(parameters : dict,session_id):
    food_items = parameters['food_item']
    quantities = parameters['number']

    if len(food_items) != len(quantities):
        fulfillmentText = "Please specify the quantities correctly for all items"
    else:
        new_food_dict = dict(zip(food_items,quantities))
        if session_id in inprogress_orders:
            current_food_dict = inprogress_orders[session_id]
            current_food_dict.update(new_food_dict)
            inprogress_orders[session_id] = current_food_dict
        else:
            inprogress_orders[session_id] = new_food_dict

        order_str = generic_helper.get_str_from_food_dict(inprogress_orders[session_id])

        fulfillmentText = f"So far You Have {order_str}. Do you need anything else ?"

    return JSONResponse(content={
        "fulfillmentText": fulfillmentText
    })

def track_order(parameters : dict,session_id):
    order_id = int(parameters['number'])
    order_status = db_helper.get_order_status(order_id)
    if order_status:
        fulfillmentText = f"The order status for order id : {order_id} is {order_status}"
    else:
        fulfillmentText = "Not Found. Please Try Again Later"

    return JSONResponse(content={
        "fulfillmentText": fulfillmentText
    })



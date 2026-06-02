def validate_side(side):
    return side.upper() in ["BUY", "SELL"]

def validate_order(order_type):
    return order_type.upper() in ["MARKET", "LIMIT"]

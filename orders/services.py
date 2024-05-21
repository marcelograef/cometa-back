from datetime import datetime

def get_stock_data():
    # this data mocked would be replace by data fro DB
    stock_data = {
        "last_updated": datetime.strptime("2024-09-10 12:00:00", "%Y-%m-%d %H:%M:%S"),
        "beers": [
            {"name": "Corona", "price": 115, "quantity": 2},
            {"name": "Quilmes", "price": 120, "quantity": 0},
            {"name": "Club Colombia", "price": 110, "quantity": 3}
        ]
    }
    return stock_data

def get_order_data():
    stock_data = get_stock_data()
    beer_prices = {beer["name"]: beer["price"] for beer in stock_data["beers"]}

    # this data mocked would be replace by data fro DB
    order_data = {
        "created": datetime.strptime("2024-09-10 12:00:00", "%Y-%m-%d %H:%M:%S"),
        "paid": False,
        "subtotal": 0,
        "taxes": 0,
        "discounts": 0,
        "items": [],
        "rounds": [
            {
                "created": datetime.strptime("2024-09-10 12:00:30", "%Y-%m-%d %H:%M:%S"),
                "items": [
                    {"name": "Corona", "quantity": 2},
                    {"name": "Club Colombia", "quantity": 1}
                ]
            },
            {
                "created": datetime.strptime("2024-09-10 12:20:31", "%Y-%m-%d %H:%M:%S"),
                "items": [
                    {"name": "Club Colombia", "quantity": 1},
                    {"name": "Quilmes", "quantity": 2}
                ]
            },
            {
                "created": datetime.strptime("2024-09-10 12:43:21", "%Y-%m-%d %H:%M:%S"),
                "items": [
                    {"name": "Quilmes", "quantity": 3}
                ]
            }
        ]
    }

    # Calculate the subtotal
    total_subtotal = 0
    for round in order_data["rounds"]:
        for item in round["items"]:
            item_name = item["name"]
            item_quantity = item["quantity"]
            item_price = beer_prices.get(item_name, 0)
            item_subtotal = item_price * item_quantity
            item["subtotal"] = item_subtotal
            total_subtotal += item_subtotal

    order_data["subtotal"] = total_subtotal

    print(order_data)
    return order_data

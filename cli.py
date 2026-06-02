from bot.orders import place_market_order, place_limit_order

symbol = input("Symbol (e.g. BTCUSDT): ").upper()
side = input("BUY or SELL: ").upper()
order_type = input("MARKET or LIMIT: ").upper()
quantity = float(input("Quantity: "))

try:
    if order_type == "MARKET":
        result = place_market_order(symbol, side, quantity)
    else:
        price = float(input("Price: "))
        result = place_limit_order(
            symbol,
            side,
            quantity,
            price
        )

    print("\nOrder placed successfully!")
    print(result)

except Exception as e:
    print("Error:", e)

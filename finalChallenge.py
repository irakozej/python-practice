def whatToBuy(prices, quantities, restriction, names):
    # Write code here
    if len(prices) == 0:
        return [[], 0]
    
    # Calculate average quantity and average price
    total_items = len(prices)
    total_quantity = sum(quantities)
    average_quantity = total_quantity / total_items
    average_price = sum(prices) / total_items
    
    # Calculate total price for each item
    total_prices = []
    for i in range(total_items):
        total_price = (quantities[i] * prices[i]) / (average_quantity * average_price)
        total_prices.append(total_price)
    
    # Find items whose total price is smaller than the restriction
    affordable_items = []
    items_removed = 0
    for i in range(total_items):
        if total_prices[i] < restriction:
            affordable_items.append(names[i])
        else:
            items_removed += 1
    
    # Sort the list of affordable items
    affordable_items.sort()
    
    return [affordable_items, items_removed]
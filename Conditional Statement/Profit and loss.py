total_cost = int(input("Enter the total cost:"))
sale_amount = int(input("Enter the sale amount:"))

if sale_amount > total_cost:
    profit = sale_amount - total_cost
    print("Profit:" , profit)


else:
    loss = total_cost - sale_amount
    print("Lost amount: " ,loss)
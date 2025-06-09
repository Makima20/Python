amount = int(input("Enter an amount:"))


note500 = amount // 500
amount = amount % 500 
note100 = amount // 100
amount = amount % 100
note50 = amount // 50
amount = amount % 50 
note10 = amount // 10
amount = amount % 10 

print("Note of 500:", note500)
print("Note of 100:", note100)
print("Note of 50:", note50)
print("Note of 10:", note10)
print("Remaining amount:", amount)


units = int(input("Enter the amount of unites consumed:"))

if units < 50:
    amount = units*5
    surchrage = 25
elif units <= 100:
    amount = units*7.5
    surchrage = 25
elif units <= 200:
    amount = units*9
    surchrage = 25
else:
    amount = units*10
    surchrage = 70

total = amount + surchrage
print("Total electricty bill :", total)


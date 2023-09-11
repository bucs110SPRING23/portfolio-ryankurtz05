rate = input("Please enter the current exchange rate between the Euro to Dollar.")
amount = input("Please enter the amount of money you want to exchange.")

total = float(rate) * float(amount)

result = total - 3

print("A Euro is worth",rate,"USD, so your",amount,"gives you $",result,"after our service fee of $3.")
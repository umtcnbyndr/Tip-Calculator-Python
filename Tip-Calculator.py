print("Welcome to the tip calculator ")
bill=input("What was the total bill? $")
tip=input("What percantage tip would you like to give? 10, 12, or 15? ")
split=(float(bill)*float(tip))/100
people=input("How many people to split the bill? ")
toplam=int(bill)+int(split)
total=toplam/int(people)
print(f"Each person should pay ${round(total)}")



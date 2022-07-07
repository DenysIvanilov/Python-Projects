print("Welcome to the tip calculator")

bill = float(input("What was the total bill? "))

tip = int(input("How much tip would you like to give?(In percent) 10, 12, or 15? "))

split = int(input("How many people to split the bill? "))

bill_after_tip = bill + bill * (tip / 100)

bill_per_person = "{:.2f}".format(bill_after_tip / split)

print(f"Each person should pay: ${bill_per_person}")
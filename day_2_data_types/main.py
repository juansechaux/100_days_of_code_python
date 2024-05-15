print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
percent_tip = float(input("How much percentage tip would you like to give? 10, 12 or 15? "))
total_people = int(input("How many people to split the bill? "))

total_bill = (bill + (bill * (percent_tip / 100)))
bill_per_person = round(total_bill / total_people,  2)
bill_per_person_format = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${bill_per_person_format}")

print("-" * 40)
print("Welcome to the tip calculator!")
print("-" * 40, '\n')

total_bill = float(input("What is the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))

price_per_person = round((total_bill * (tip/100) + total_bill)/num_of_people, 2)
print(f"Each person should pay: ${price_per_person}")
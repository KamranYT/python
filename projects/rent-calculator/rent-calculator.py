print("Welcome to Rent_Calculator")

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total units of elctricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat - "))

electricity_bill = electricity_spend * charge_per_unit

output = (food + rent + electricity_bill) // persons

print("Each person will pay = ", output)
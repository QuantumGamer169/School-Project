#Main Menu
print("(------------Main Menu------------)")
print("1. Enter airport details")
print("2. Enter flight details")
print("3. Enter price plan and calculate profit")
print("4. Clear data")
print("5. Quit")
print("Please enter a number.")
choice = int(input("Choose an option: "))

#Main menu While loop and error checker
while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
	choice = int(input("Error, enter 1, 2, 3, 4 or 5: "))
if choice == 1:
	print("(------------Enter_airport_details------------)")
elif choice == 2:
	print("(------------Enter_flight_details------------)")
elif choice == 3:
	print("(------------Enter_price_plan_and_calculate_profit------------)")
elif choice == 4:
	print("(------------Clear_data------------)")
elif choice == 5:
	print("(------------Quit------------)")
	print("(------------GoodBye------------)")
else:
	print("(------------Invalid------------)")

Main Menu
print("(------------Main Menu------------)")
print("1. LPL: ")
print("2. BOH")
print("Please enter a number.")
choice = int(input("Choose an option: "))

#Main menu While loop and error checker
while choice != 1 and choice != 2:
	choice = int(input("Error, enter 1 or 2: "))
if choice == 1:
	print("(------------1------------)")
  #opens the airports.txt
  file = open("Airports.txt", "r")
  for i in range (5):
  line = file.readline()
  data = line.split(",")
  #print (data[0])
  #print (data[0:4])
  #find the overseas info for the airport
  if  data[0] == OverSeas_Airport:
    print (data[0:4])
  file.close()
  #
elif choice == 2:
	print("(------------2------------)")
  #opens the airports.txt
  file = open("Airports.txt", "r")
  for i in range (5):
  line = file.readline()
  data = line.split(",")
  #find the overseas info for the airport
  if  data[0] == OverSeas_Airport:
    print (data[0:4])
  file.close()
  #
else:
	print("(------------Invalid------------)")


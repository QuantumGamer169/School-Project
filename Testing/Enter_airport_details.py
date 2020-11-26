choice = str(input("Please enter a 3 letter code: "))

# Main menu While loop and error checker
while choice != ("LPL") and choice != ("BOH"):
    choice = str(input("Error, enter 1 or 2: "))

OverSeas_Airport = input(str("Enter the overseas airport code:  "))


file = open("Airports.txt", "r")
lines = file.readlines()
#lines now refers to a list 
#with each element of the list holding one record
#Find the number of lines in the list
numberOfRecs = len(lines)
print("There are ",numberOfRecs," elements in the list")


for n in range(numberOfRecs):
  line = file.readline()
  data = line.split(",")
  print(data)
  if data[0] == ("OverSeas_Airport"):
    print (data[1])

file.close()


#ask the user for uk and overseas idetifiers 
UK_Airport = str(input("Please enter a 3 letter idetifier for uk airport:    "))
UK_Airport = (UK_Airport.upper())
OverSeas_Airport = str(input("Please enter a 3 letter idetifier for overseas airport:    "))
OverSeas_Airport = (OverSeas_Airport.upper())

#opens the airports.txt
file = open("Airports.txt", "r")

#checks UK_Airport For the uk indetifiers 
if UK_Airport == ("LPL"):
  for i in range (5):
    line = file.readline()
    data = line.split(",")
    #print (data[0])
    #print (data[0:4])
    #find the overseas info for the airport
    if  data[0] == OverSeas_Airport:
      print (data[0:4])
elif UK_Airport == ("BOH"):
  for i in range (5):
    line = file.readline()
    data = line.split(",")
    #find the overseas info for the airport
    if  data[0] == OverSeas_Airport:
      print (data[0:4])

file.close()

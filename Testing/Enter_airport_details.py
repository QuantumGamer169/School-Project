UK_Airport = str(input("Please enter a 3 letter idetifier for uk airport:    "))
UK_Airport = (UK_Airport.upper())
OverSeas_Airport = str(input("Please enter a 3 letter idetifier for overseas airport:    "))
OverSeas_Airport = (OverSeas_Airport.upper())
file = open("Airports.txt", "r")
if UK_Airport = ("LPL"):
  for i in range (5):
  line = file.readline()
  data = line.split(",")
  if  data[0] == OverSeas_Airport:
    print (data[0:4])
elif UK_Airport = ("BOH"):
  for i in range (5):
  line = file.readline()
  data = line.split(",")
  if  data[0] == OverSeas_Airport:
    print (data[0:4])



file.close()

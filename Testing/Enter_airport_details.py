input1 = str(input("Please enter a 3 letter idetifier:    "))
file = open("Airports.txt", "r")
for i in range (5):
  line = file.readline()
  data = line.split(",")
  if  data[0] == input1:
    print (data[0:4])



file.close()

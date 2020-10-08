file = open("Airports.txt", "r")
for i in range (5):
  line = file.readline()
  data = line.split(",")
  print (data)

file.close()

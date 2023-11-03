# Read in the data

myFile = open("advent2.txt")

myData = myFile.read().splitlines()

print(myData)


z=0
x=0
final=0
aim=0
for i in range(len(myData)):
  if str(myData[i][0])== "f":
    z= z+int(myData[i][-1])
    x= x + aim*int(myData[i][-1])
  if str(myData[i][0])== "u":
    aim= aim-int(myData[i][-1])
  if str(myData[i][0])== "d":
    aim= aim+int(myData[i][-1])
print(z)
print(x)
final=z*x
print(final)
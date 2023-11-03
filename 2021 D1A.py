# Read in the data
#1676
myFile = open("advent1a.txt")

myData = myFile.read().splitlines()


count=0
for i in range(len(myData)-1):
  if(int(myData[i])<int(myData[i+1])):
    count=count+1
print(count)
#loop through the list and count increasing


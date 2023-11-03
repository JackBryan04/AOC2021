myFile = open("advent1b.txt")

myData = myFile.read().splitlines()

counting=0
for i in range(len(myData)-3):
  sum=int(myData[i])+int(myData[i+1])+int(myData[i+2])
  sum0=int(myData[i+1])+int(myData[i+2])+int(myData[i+3])
  if int(sum)<int(sum0):
    counting=counting+1
print(counting)
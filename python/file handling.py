'''
open(filename, mode)

r = read
r+ = read and write
w = write - overwrites an existing file
a = append - does not overwrite existing file
'''

filename = "Vacation.txt"
vacationPlaces = ["London", "Paris", "Los Angeles", "New York", "Tokyo"]
myFile = open(filename, 'w')
#myFile = open(r'\Volumes\Kriti-1\nacations.txt', 'w')
myFile = open('/Volumes/Kriti-1/Vacations.txt', 'w')

for place in vacationPlaces:
    myFile.write(place + '\n')

myFile.close()


myFile = open(filename, 'r')
#fileContent = myFile.read() #Reads in one go
#print(fileContent)

# for line in myFile: #Read line by line
#     print(line)

print(myFile.readline())
print(myFile.readline())

myFile.close()


myFile = open('Vacation.txt', 'a')
myFile.write("Mumbai")
myFile.close()

'''
with open('Vacation.txt', 'w') as myFile:
    myFile.write("Hi!")
'''
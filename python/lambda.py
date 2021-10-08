l1 = list(range(1, 11))

def times10(x):
    return x * 10

def checkForEven(x):
    if x%2 == 0:
        return True
    else:
        return False

# for i in l1:
#     print(times10(i))

#output = list(map(times10, l1))

output = list(map(lambda x : x * 10 ,l1))
print(output)

evenNumbers = list(filter(lambda x : x%2 == 0, l1))
print(evenNumbers)
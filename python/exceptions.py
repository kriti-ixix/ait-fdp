try:
    myList = [1, 2, 3, 4, 5]
    userChoice = int(input("Enter the index: "))
    print("The value is", myList[userChoice])
    #print(myList[3])
    #print(myList[10])

except ValueError:
    print("Please enter a valid index")

except IndexError:
    print("The index does not exist")

except:
    print("Error")

finally:
    print("End of execution")

class ValueTooSmallError(Exception):
    def __init__(self, message="Error"):
        self.message = message

    def __str__(self):
        return self.message

class ValueTooLargeError(Exception):
    pass

number = 10

try:
    guess = int(input("Enter some guess: "))

    if guess > number:
        raise ValueTooLargeError()
    elif guess < number:
        raise ValueTooSmallError("There was some error")
    else:
        print("Guess was correct!")

except ValueTooSmallError as e:
    #print("Value was too small")
    print(e)

except ValueTooLargeError:
    print("Value was too large")

except:
    print("Error")
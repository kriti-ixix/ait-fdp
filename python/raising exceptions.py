try:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))

    if length < 0 or breadth < 0:
        raise ValueError

    area = length * breadth
    print("Area is", area)

except:
    print("Length or breadth cannot be negative")
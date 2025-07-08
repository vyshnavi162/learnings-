num = int(input("Enter a number: "))
square = num ** 2
if str(square).endswith(str(num)):
    print("Automorphic number")
else:
    print("Not an Automorphic number")
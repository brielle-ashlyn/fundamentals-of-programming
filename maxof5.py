print("Please enter five integer values")
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
n4 = int(input("Number 4: "))
n5 = int(input("Number 5: "))
if n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5:
    print("The Maximum is: ", n1)
elif n2 >= n3 and n2 >= n4 and n2 >= n5:
    print("The Maximum is: ", n2)
elif n3 >= n4 and n3 >= n5:
    print("The Maximum is: ", n3)
elif n4 >= n5:
    print("The Maximum is: ", n4)
elif n4 <= n5:
    print("The Maximum is: ", n5)



v = float(input("Enter voltage (V): "))
a = float(input("Enter current (A): "))
h = float(input("Enter operating time (h): "))
print("The cost is {:.2f}".format((((v*a) * h) * 4)/1000))
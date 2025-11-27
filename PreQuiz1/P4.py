v = float(input("Enter voltage (V): "))
a = float(input("Enter current (A): "))
h = float(input("Enter operating time (h): "))
print(f"The cost is {(((v*a) * h) * 4)/1000}")
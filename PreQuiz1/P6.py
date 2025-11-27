a = float(input("a: "))
b = float(input("b: "))
if a == 0 and b == 0:
    print("a/b = Not defined")
elif a < 0 and b == 0:
    print("a/b = Negative infinity")
elif a > 0 and b == 0:
    print("a/b = infinity")
else :
    print(f"a/b = {a/b:.1f}")
import math

n = int(input("Number of values:"))
sic = 0
for i in range(n):
    x = float(input("value:"))
    sic += x**2
rms = math.sqrt((1/n) * sic)

print("RMS = {:,.2f}".format(rms))
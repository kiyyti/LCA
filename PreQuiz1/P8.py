import math as m

n = int(input("Number of values:"))
sic = 0
for i in range(n):
    x = float(input("value:"))
    sic += x**2
rms = m.sqrt((1/n) * sic)

print(f"RMS = {rms:,.2f}")
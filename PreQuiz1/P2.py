watt = float(input("Enter power in watt:"))
hours = float(input("Enter operating hours:"))

print(f"Energy = {watt*hours:,.2f} Wh or {3600 * (watt * hours):,.2f} J")
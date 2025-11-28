if __name__ == "__main__":
    watt = float(input("Enter power in watt:"))
    hours = float(input("Enter operating hours:"))

    print("Energy = {:,.2f} Wh or {:,.2f} J".format(watt*hours, 3600 * (watt * hours)))
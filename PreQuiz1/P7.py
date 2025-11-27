import math as m

def rec_to_pol(a, b):
    ra = m.atan2(b,a) 
    po = m.sqrt(a**2 + b**2)
    de = m.degrees(ra)
    return de, po


def main():
    x, y = map(float,input("Enter (x y):").split())
    degree, polar = rec_to_pol(x,y)
    print(f"polar: {polar:.2f} with {degree:.2f} degree")
main()
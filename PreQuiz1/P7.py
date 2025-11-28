import math

def rec_to_pol(a, b):
    ra = math.atan2(b,a) 
    po = math.sqrt(a**2 + b**2)
    de = math.degrees(ra)
    return de, po


def main():
    x, y = map(float,input("Enter (x y):").split())
    degree, polar = rec_to_pol(x,y)
    print("polar: {:.2f} with {:.2f} degree".format(polar,degree))
main()
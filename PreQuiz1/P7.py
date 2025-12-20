#change

import math 

def rec_to_pol(a, b):
    po = math.sqrt(a**2 + b**2)
    de = math.degrees(math.atan2(b,a))
    if de < 0:
        de += 360
    return po, de

if __name__ == '__main__':
    r, c = input('Enter (x y):').split()
    m, a = rec_to_pol(float(r), float(c))
    print("polar: {:.2f} with {:.2f} degree".format(m, a))
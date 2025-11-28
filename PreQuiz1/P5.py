# change

def power_equiv(pwat) :
    hp = float(pwat) / 745.7
    btum = float(pwat) / 0.293
    calm = float(pwat) * 14.33
    erg = float(pwat) * 1e7
    flbm = float(pwat) * 44.25
    return hp, btum, calm, erg, flbm

if __name__ == '__main__':
    pwatt = input()
    horsep, btuh, calmin, perg, footlbm = power_equiv(pwatt)
    print(pwatt, 'w =', round(horsep,3), 'hp =',
    round(btuh,3), 'btu/h =',
    round(calmin,3),'cal/min =',
    round(perg,3), 'erg =',
    round(footlbm,3), 'f-lb/min')
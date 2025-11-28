def power_equiv(pwat) :
    hr = pwat / 745.7
    btuh = pwat / 0.293
    calmin = pwat * 14.33
    perg = pwat * 1e7
    flbm = pwat * 44.25
    return hr, btuh, calmin, perg, flbm

def main():
    pwatt = float(input())
    horsep, btuh, calmin, perg, footlbm = power_equiv(pwatt)
    print(pwatt, 'w =', round(horsep,3), 'hp =',
    round(btuh,3), 'btu/h =',
    round(calmin,3),'cal/min =',
    round(perg,3), 'erg =',
    round(footlbm,3), 'f-lb/min')
main()
Cpt = int(input("Battery capacity (mAh):"))
Cpt_Ah = Cpt / 1000
Wh = Cpt_Ah * 12

# Don't edit below this line.
# ================================================================
print('At its 12 V rating, it stores %.2f Wh.'%Wh)
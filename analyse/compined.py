e_w=2700
e_b=2600

if e_w>e_b:
    e_st=e_w
    e_wo=e_b

else:
    e_st=e_b
    e_wo=e_w

dif=e_st-e_wo

r_w=((5.80944*10**-7)*e_st**2-0.002214*e_st+2.3048)*(-8*10**-4*dif+1)

print(r_w)
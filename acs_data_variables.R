#year20xx ACS 
# population table B01
# population in that year
pop20xx=B00001e1
# population under 18
pop2010_under18=B01001e3+B01001e4+B01001e5+B01001e6+B01001e27+B01001e28+B01001e29+B01001e30
# population over 65
pop2010_over65=B01001e20+B01001e21+B01001e22+B01001e23+B01001e24+B01001e25+B01001e44+B01001e45+B01001e46+B01001e47+B01001e48+B01001e49
# median age
median_age=B01002e1

#Home value table B25
med_hom_value=B19013e1
# %Home less than 100,000
pct_hom_less10grants=(B25075e2+B25075e3+B25075e4+B25075e5+B25075e6+B25075e7+B25075e8+B25075e9+B25075e10+B25075e11+B25075e12+B25075e13+B25075e14)/B25075e1
# %home vacant
hom_vacant=B25004e1/B25001e1
# &home seasonal
hom_seasonal=B25004e6/B25001e1
# households lacking complete plumbing facilites
house_lack_plumb=B25016e7+B25016e16

# Income table B19
# median income household
med_income=B19013e1
# % household w retirement income
pct_w_retire_income=B19059e2/B19001e
# % household w social security income
pct_w_ss_income=B19055e2/B19001e1

# Employment table 24
# Umemployment rate
pct_umemploy=B23025e5/B23025e3
# % of population in labor force
pct_pop_labor=B23025e2/B23025e1
# % employment in agriculture, forest, fish industry
pct_employ_agr_for_fis=(C24030e3+C24030e30)/c24030e1
# % employment in arts, entertainment, and recreation, and accommodation and food service
pct_employ_arts=(C24030e24+c24030e51)/C24030e1
# % employment in retail trade
pct_employ_retail=(C24030e9+C24030e36)/C24030e1

# soial status table c17
# % of people below poverty line
pct_poverty=(C17002e3+C17002e2)/C17002e1

# % househod w SNAP table B22
pct_house_snap=B22010e2/B22010e1

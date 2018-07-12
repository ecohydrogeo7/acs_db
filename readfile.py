import pandas as pd
from pandas import DataFrame

#filename = ["acs2010.txt","acs2011.txt","acs2012.txt","acs2013.txt","acs2014.txt","acs2015.txt","acs2016.txt"]
filename = ["acs2011.txt","acs2016.txt"]
for fn in filename:
    data = pd.read_csv(fn, index_col=0)
    # convert NA to zero
    #data.fillna(0)
    #data["B010013"].fillna(0)
    newdata: DataFrame = pd.DataFrame()
    newdata["GID"] = data["GEOID_Data"]
    newdata["pop"] = data["B01001e1"]
    newdata["pop_under18"] = data["B01001e3"]+data["B01001e4"]+data["B01001e5"]+data["B01001e6"]+data["B01001e27"]+data["B01001e28"]+data["B01001e29"]+data["B01001e30"]
    newdata["pop_over65"] = data["B01001e20"]+data["B01001e21"]+data["B01001e22"]+data["B01001e23"]+data["B01001e24"]+data["B01001e25"]+data["B01001e44"]+data["B01001e45"]+data["B01001e46"]+data["B01001e47"]+data["B01001e48"]+data["B01001e49"]
    newdata["median_age"]= data["B01002e1"]
    newdata["med_home_value"]= data["B19013e1"]
    newdata["pct_home_less100grants"]=(data["B25075e2"]+data["B25075e3"]+data["B25075e4"]+data["B25075e5"]+data["B25075e6"]+data["B25075e7"]+data["B25075e8"]+data["B25075e9"]+data["B25075e10"]+data["B25075e11"]+data["B25075e12"]+data["B25075e13"]+data["B25075e14"])/data["B25075e1"]
    newdata["home_vacant"]= data["B25004e1"]/(data["B25001e1"] + 0.000001)
    newdata["home_seasonal"]= data["B25004e6"]/(data["B25001e1"] + 0.000001)
    try:
        newdata["pct_house_lack_plumb"]=(data["B25016e7"]+data["B25016e16"])/(data["B25001e1"] + 0.000001)
    except:
        pass
    try:
        newdata["pct_w_retire_income"]=data["B19059e2"]/(data["B19001e"] + 0.000001)
    except:
        pass
    newdata["med_income"]=data["B19013e1"]
    newdata["pct_w_ss_income"]=data["B19055e2"]/(data["B19001e1"] + 0.000001)

    try:
        newdata["pct_unemploy"] = data["B23025e5"] / (data["B23025e3"] + 0.000001)
    except:
        pass
    try:
        newdata["pct_pop_labor"]=data["B23025e2"]/(data["B23025e1"] + 0.000001)
    except:
        pass
    try:
        newdata["pct_employ_agr_for_fis"]=(data["C24030e3"]+data["C24030e30"])/(data["C24030e1"] + 0.000001)
    except:
        pass
    try:
        newdata["pct_employ_arts"]=(data["C24030e24"]+data["C24030e51"])/(data["C24030e1"] + 0.000001)
    except:
        pass
    try:
        newdata["pct_employ_retail"]=(data["C24030e9"]+data["C24030e36"])/(data["C24030e1"] + 0.000001)
    except:
        pass
    newdata["pct_poverty"]=(data["C17002e3"]+data["C17002e2"])/(data["C17002e1"] + 0.000001)
    try:
        newdata["pct_house_snap"]=data["B22010e2"]/(data["B22010e1"] + 0.000001)
    except:
        pass
    newdata.to_csv("n_stats_"+ fn, sep=",")
    #print(data)

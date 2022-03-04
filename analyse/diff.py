#Berechnet die Graphen für ELOs

# importing mplot3d toolkits, numpy and matplotlib
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pandas as dp
import pandas


graph={}
fac=20

df=dp.read_csv("raw.csv")
diff=400

df=df[(df.dif<diff)]
df=df[(df.dif>-diff)]

df=df[(df.av>2600)]
df=df[(df.av<2800)]
df=df.reindex()
df["dif"]=abs(df["dif"])
df=df.sort_values(by="dif")

for idx, row in df.iterrows():
    dif=abs(row["dif"])
    re=row["res"]

    if dif in graph:
        graph[dif]["acc"]=graph[dif]["acc"]+1

        if re==0.5:
            graph[dif]["r"]+=1
        else:
            graph[dif]["o"]=graph[dif]["o"]+1

    else:
        graph[dif]={"r":0, "o":0, "acc":1}

difs=[]
for dif in graph:
    difs.append(dif)

graphs={}
i=len(difs)-1
while i>0+fac:
    dif=difs[i]
    r=0
    o=0
    acc=0
    for sub in range(fac):
        dif=difs[i-sub]
        r+=graph[dif]["r"]
        o+=graph[dif]["o"]
        acc+=graph[dif]["acc"]
    graphs[dif]={"r":r, "o":o, "acc":acc}
    i-=fac

gr=pandas.DataFrame.from_dict(graphs)
gr=gr.T
gr["dif"]=gr.index

gr["r_a"]=gr["r"]/(gr["r"]+gr["o"])
gr["r_c1"]=-gr["dif"]*8*10**-4+1

gr.plot(x="dif", y=["r_a", "r_c1"], kind="line")
plt.show()
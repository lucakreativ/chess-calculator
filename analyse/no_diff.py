import pandas
import matplotlib.pyplot as mp


graph={}
fac=20

data=pandas.read_csv("raw.csv")
data.sort_values(
    ascending=False,
    axis=0,
    by="w_elo",
    inplace=True
)

diff=20

data=data[(data.dif<diff)]
data=data[(data.dif>-diff)]

data=data[(data.w_elo>1800)]
data=data[(data.w_elo<2800)]
data=data.reindex()

for idx, row in data.iterrows():
    w_elo=row["w_elo"]
    re=row["res"]

    if w_elo in graph:
        graph[w_elo]["acc"]=graph[w_elo]["acc"]+1

        if re==0.5:
            graph[w_elo]["r"]+=1
        else:
            graph[w_elo]["o"]=graph[w_elo]["o"]+1

    else:
        graph[w_elo]={"r":0, "o":0, "acc":1}

elos=[]
for elo in graph:
    elos.append(elo)

graphs={}
i=len(elos)-1
while i>0+fac:
    elo=elos[i]
    r=0
    o=0
    acc=0
    for sub in range(fac):
        elo=elos[i-sub]
        r+=graph[elo]["r"]
        o+=graph[elo]["o"]
        acc+=graph[elo]["acc"]
    graphs[elo]={"r":r, "o":o, "acc":acc}
    i-=1
    #print(i)


gr=pandas.DataFrame.from_dict(graphs)
gr=gr.T
gr["elo"]=gr.index




gr["r_a"]=gr["r"]/(gr["r"]+gr["o"])
gr["r_c1"]=(4.09*10**-7)*gr["elo"]**2-0.001375*gr["elo"]+1.3
gr["r_c2"]=(5.241*10**-7)*gr["elo"]**2-0.0019*gr["elo"]+1.872
gr["r_c3"]=(4.873*10**-7)*gr["elo"]**2-0.00173*gr["elo"]+1.6888
gr["r_c4"]=(5.80944*10**-7)*gr["elo"]**2-0.002214*gr["elo"]+2.3048

#print(gr)
gr.plot(x="elo", y=["r_a", "r_c1","r_c2", "r_c3", "r_c4"], kind="line")
mp.show()
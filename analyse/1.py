import pandas
import matplotlib.pyplot as mp


graph={}
fac=20

data=pandas.read_csv("data.csv")
data.sort_values(
    ascending=False,
    axis=0,
    by="w_elo",
    inplace=True
)

diff=50

data=data[(data.dif<diff)]
data=data[(data.dif>-diff)]

data=data[(data.w_elo>1750)]
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
    i-=fac
    #print(i)


gr=pandas.DataFrame.from_dict(graphs)
gr=gr.T
gr["elo"]=gr.index




gr["r_a"]=gr["r"]/(gr["r"]+gr["o"])
gr["r_c"]=(4.09*10**-7)*gr["elo"]**2-0.001375*gr["elo"]+1.3

#print(gr)
gr.plot(x="elo", y=["r_a", "r_c"], kind="line")
mp.show()
import re
import pandas

events=["Candidates", "Sinquefield Cup", "Tata Steel", "World Cup", "Grand Prix", "Dutch League", "Biel", "Olympiad"]


f=open("reduced.pgn")
data=f.read()
f.close()


data=data.split("\n")

def get_string(line):
    string=re.sub('''\[.* "''', string=line,repl="")
    string=re.sub('''"\]''', string=string ,repl="")
    return string

whiteelo=None
blackelo=None
result=None
count=0

l_we=[]
l_be=[]
l_r=[]
l_a=[]
l_d=[]

for line in data:
    if re.search('''\[Event "''', line):
        event=get_string(line)

    if re.search('''\[White "''', line):
        white=get_string(line)
        #print("White: "+white)

    if re.search('''\[Black "''', line):
        black=get_string(line)
        #print("Black: "+black)


    if re.search('''\[Result "''', line):
        result=get_string(line)
        #print("Result: "+result)


    if re.search('''\[WhiteElo "''', line):
        whiteelo=get_string(line)
        #print("WhiteElo: "+whiteelo)

    if re.search('''\[BlackElo "''', line):
        blackelo=get_string(line)
        #print("BlackElo: "+blackelo)

    if whiteelo!=None and blackelo!=None and result!=None:
        for p_ev in events:
            if p_ev in event:
                count+=1
                print(count)
                whiteelo=int(whiteelo)
                blackelo=int(blackelo)
                av=(whiteelo+blackelo)/2
                dif=whiteelo-blackelo

                if result=="1/2-1/2":
                    result=0.5
                elif result=="1-0":
                    result=1
                elif result=="0-1":
                    result=0


                l_we.append(whiteelo)
                l_be.append(blackelo)
                l_r.append(result)
                l_a.append(av)
                l_d.append(dif)

                whiteelo=None
                blackelo=None
                result=None

data_p=pandas.DataFrame({"w_elo":l_we, "b_elo":l_be, "res":l_r, "av":l_a, "dif":l_d})

data_p.to_csv("data.csv")
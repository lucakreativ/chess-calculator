from logging.config import fileConfig
import re
import os



write=[]

def get_string(line):
    string=re.sub('''\[.* "''', string=line,repl="")
    string=re.sub('''"\]''', string=string ,repl="")
    return string

counter=0
for root, directories, file in os.walk("file/"):
    for file in file:
        counter+=1
        print(counter)
        print(file)
        f=open("file/"+file, encoding="utf8", errors="ignore")
        data=f.read()
        f.close()

        data=data.split("\n")

        for line in data:
            if re.search('''\[Event "''', line):
                write.append(line)

            if re.search('''\[White "''', line):
                write.append(line)

            if re.search('''\[Black "''', line):
                write.append(line)


            if re.search('''\[Result "''', line):
                write.append(line)


            if re.search('''\[WhiteElo "''', line):
                write.append(line)

            if re.search('''\[BlackElo "''', line):
                write.append(line)


st=""
for writer in write:
    st+=writer+"\n"

f=open("reduced.pgn", "w")
f.write(st)
f.close()
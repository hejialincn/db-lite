from function import *
import re

def re1(name,code,clumon,data,fu):
    co = r"\w+"
    command = re.match(co, code)
    if command:
        for i in data:
            for a in zip(clumon, i):
                if a[0]== name :
                    exec(f"v{a[0]} = '{a[1]}'")
                    if eval(f"v{a[0]}{fu}'{code}'"):
                        print(str(i).replace(",","|").replace("[","").replace("]","").replace(" ",""))
    else:
        for i in data:
            for a in zip(clumon, i):
                if a[0]== name :
                    exec(f"v{a[0]} = {a[1]}")
                    if eval(f"v{a[0]}{fu}{code}"):
                        print(str(i).replace(",","|").replace("[","").replace("]","").replace(" ",""))
def jie(stri):
    str_dict={}
    string=stri.split()
    for i in range(len(string)-1):
        if i%2==0:
            str_dict[string[i]]=string[i+1]
    return(str_dict)
def get(string):
    k=[]
    name=[]
    type=[]
    string=string.split(";")
    for i in string:
        k=i.split(",")
        name.append(k[0])
        type.append(k[1])
    return([name,type])
def get1(string):
    k=[]
    type=[]
    string=string.split(";")
    for i in string:
        k=i.split(",")
        type.append(k)
    print(type)
    return(type)
def func(list):
    if list[0][0]=="create":
            if list[0][1]=="table":
                if list[2][0]=="values":
                    write_json(get(list[2][1])[0],get(list[2][1])[0],[[]],list[1][1])
    if list[0][0]=="insert":
        if list[0][1]=="into":
            if list[2][0]=="values":
                change(list[1][1],get1(list[2][1]))
    if list[0][0]=="select":
        if list[0][1]=="*":
            if list[1][0]=="from" and len(list)==2:
                for i in test()[list[1][1]]['data']:
                    print(str(i).replace(",","|").replace("[","").replace("]","").replace(" ",""))
    if list[0][0] == "select":
        if list[0][1] == "*":
            if len(list)==3 and list[2][0] == "where":
                code = r"(\w+|\d+)(<=|==|>=|<|>)(\w+|\d+)"
                command = re.match(code, list[2][1])
                if command:
                    left = command.group(1)
                    middle = command.group(2)
                    right = command.group(3)
                    
                    k = []
                    for i in test()["s1"]['clumon'].keys():
                        k.append(i)
                    re1(left, right, k, test()["s1"]['data'], middle)

def use(dict):
    new1=[]
    for (key,value) in dict.items():
        new1.append([key,value]) 
    return(new1)
def main():
    i=1
    while True:
        str=input("db-lite {}>>".format(i))
        if str==".exit":
            break
        if ' ' in str and str.count(" ")>2:
            func(use(jie(str)))
        if str==".help":
            print("""create table new (name) value (values)
insert into table (name) values (value)
select * from (name)
.exit
.help               """)
        i=i+1
main()
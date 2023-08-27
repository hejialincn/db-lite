import json

def table_json(table):
    data_array = []
    for row in table[1:]:
        data_array.append(row)
    return data_array
def main(table):
    name="main"
    json_data={name:table_json(table)}
    json_data = json.dumps(json_data, indent=4)
    with open('/home/hejialin/db-lite/array_data.json',"a") as file:
        file.write(json_data)
def test():
    with open('/home/hejialin/db-lite/array_data.json', "r") as file:
        connect = file.read()
    if connect.strip() == "":
        return {}
    connect = json.loads(connect)
    return dict(connect)

def test2(name,type,array):
    table={}
    clumon={}
    for i in range(len(name)):
        clumon[name[i]]=type[i]
    table["clumon"]=clumon
    table["data"]=array
    return(table)
def test3(dict):
    with open('/home/hejialin/db-lite/array_data.json',"w") as file:
            file.write(json.dumps(dict,indent=4))
def write_json(name,type,data,name1):
    dict={}
    dict=test()
    connect=test2(name,type,data)
    dict[name1]=connect
    test3(dict)
def changerow(name,row,line):
    array=[]
    dict=test()
    array=dict[name]['data']
    array[line-1]=row
    dict[name]['data']=array
    test3(dict)
def change(name,new):
    dict=test()
    dict[name]['data']=dict[name]['data']+new
    test3(dict)
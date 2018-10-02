import json
import pandas as pd
import itertools

inputjson = open('testTransaction.json','r')
filterfile = open('customerfilter.csv','r')
outfile = open('newcustomer.csv','w')

data = json.load(inputjson)
filterdata = []
jsondata = data[0]
datafrm = pd.DataFrame(columns=['fields','values'])
global_counter1 = itertools.count()

#for line in filterfile:
#    filterdata.append((line.replace('"','')).replace('\n',''))

#def filters(filters, keystr, value):
#    for data in range(len(filters)):
#        if filters[data] == keystr:
#            process_str(keystr, value)

def process_str(keystring, value, datafrm):
    next_id = next(global_counter1)
    datafrm.loc[next_id] = [keystring,value]
    outfile.write('"{}","{}"\n'.format(keystring, value))


def process_list(keystring, value, datafrm):
    counter = 0
    for item in range(len(value)):
        if type(value[item]) not in [list, dict]:
            counter += 1
            key_counter = keystring+"_"+str(counter)
            process_str(key_counter, value[item], datafrm)
        if type(value[item]) is dict:
            process_dict(keystring, value[item], datafrm)
        if type(value[item]) is list:
            process_list(combined_key, value[item], datafrm)


def process_dict(key, value, datafrm):
    for key1, val1 in value.items():
        combined_key = key+"."+key1 
        if type(val1)  not in [list, dict]:
            process_str(combined_key, val1, datafrm)      
        if type(val1) is list:
            process_list(combined_key, val1, datafrm)
        if type(val1) is dict:
            process_dict(combined_key, val1, datafrm)



for key,val in jsondata.items():
    if type(val)  not in [list, dict]:
        process_str(key, val, datafrm)
    if type(val) is list:
        #print(key, val)
        process_list(key, val, datafrm)
    if type(val) is dict:
        process_dict(key, val, datafrm)        
    

inputjson.close()
filterfile.close()
outfile.close()
writer = pd.ExcelWriter('PythonExport.xlsx')
datafrm.to_excel(writer,'Sheet1')
writer.save()

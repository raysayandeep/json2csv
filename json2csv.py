import json


inputjson = open('newcustomer.json','r')
filterfile = open('customerfilter.csv','r')
outfile = open('newcustomer.csv','w')

data = json.load(inputjson)
filterdata = []
jsondata = data[0]

for line in filterfile:
    filterdata.append((line.replace('"','')).replace('\n',''))

def filters(filters, keystr, value):
    for data in range(len(filters)):
        if filters[data] == keystr:
            process_str(keystr, value)

def process_str(keystring, value):
    outfile.write('"{}","{}"\n'.format(keystring, value))


def process_list(keystring, value):
    counter = 0
    for item in range(len(value)):
        if type(value[item]) is str:
            counter += 1
            key_counter = keystring+"_"+str(counter)
            process_str(key_counter, value[item])
        if type(value[item]) is int:
            counter += 1
            key_counter = keystring+"_"+str(counter)
            process_str(key_counter, str(value[item]))
        if type(value[item]) is dict:
            process_dict(keystring, value[item])


def process_dict(key, value):
    for key1, val1 in value.items():
        combined_key = key+"."+key1 
        if type(val1) is str:
            process_str(combined_key, val1)
        if type(val1) is int:
            process_str(combined_key, val1)        
        if type(val1) is list:
            process_list(combined_key, val1)
        if type(val1) is dict:
            process_dict(combined_key, val1)


for key,val in jsondata.items():
    if type(val) is str:
        process_str(key, val)
    if type(val) is list:
        #print(key, val)
        process_list(key, val)
    if type(val) is dict:
        process_dict(key, val)         
    

inputjson.close()
filterfile.close()
outfile.close()

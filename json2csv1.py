import json
import csv

js = open('newcustomer.json','r')
jsp = open('newcustomer1.json','w')
data = json.load(js)
json.dump(data, jsp, indent=4)
js.close()
jsp.close()

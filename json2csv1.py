import json
import csv

js = open('testtransaction.json','r')
jsp = open('testTransaction.json','w')
data = json.load(js)
json.dump(data, jsp, indent=4)
js.close()
jsp.close()

import sys
import csv

template = sys.argv[1]
datafile = sys.argv[2]

with open(template,"r",encoding = "utf_8_sig") as t:
    template_data = t.read()

with open(datafile,"r",encoding = "utf_8_sig") as d:
    f = csv.DictReader(d, dialect=csv.excel)
    for row in f:
        output = template_data
        for k in row.keys():
            output = output.replace(k,row[k])
        print(output)

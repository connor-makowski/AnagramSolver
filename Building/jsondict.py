import csv
import json

filelocation=(r'.\words_alpha.csv')
jsonlocation=(r'.\words.json')
with open(filelocation) as csvfile:
    list = csv.reader(csvfile, delimiter=',')
    dictionary={}
    for word in list:
        fl=word[0][:1]
        if fl not in dictionary:
            dictionary[fl]=[]
        dictionary[fl].append(word[0])

with open(jsonlocation, 'w') as fp:
    json.dump(dictionary, fp)

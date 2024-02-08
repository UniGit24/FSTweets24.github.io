import json
 
# Opening JSON file
f = open('bbc_news_list_uk.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data['news']:
    if "Australia" in i['title']:
        print(i['title'])
    if "US" in i['title']:
        print(i['title'])
    if "Canada" in i['title']:
        print(i['title'])
 
# Closing file
f.close()


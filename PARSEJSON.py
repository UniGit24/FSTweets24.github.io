import json
 
# Opening JSON file
f = open('bloomberg_quint_news (1).json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
listtopics = []
for i in data['news']:
    if "Australia" in i['title']:
            if "June 2021" or "July 2021" or "August 2021" or "Septemebr 2021" or "October 2021" in i['date_created']:
                listtopics.append(i['title'])
                print(i['title'])
            else:
                print(" ")
    #if "US" in i['title']:
    #    print(i['title'])
    #if "Canada" in i['title']:
    #    print(i['title'])
print(listtopics)
# Closing file
f.close()
def function():
    if "June 2021" in i['date_created']:
            print(i['title'])
    else:
        print(" ")
    if "July 2021" in i['date_created']:
        print(i['title'])
    else:
        print(" ")
    if "August 2021" in i['date_created']:
        print(i['title'])
    else:
        print(" ")
    if "September 2021" in i['date_created']:
        print(i['title'])
    else:
        print(" ")
    if "October 2021" in i['date_created']:
        print(i['title'])
    else:
        print(" ")


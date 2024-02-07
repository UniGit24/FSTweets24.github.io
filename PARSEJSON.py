import json

with open('bbc_news_list_uk.json') as f:
  data = json.load(f)
print(data)

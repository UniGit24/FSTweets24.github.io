import requests

base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': 'zbdiss', 'password': 'ucldiss23'}
auth = requests.auth.HTTPBasicAuth('39KRf3EvLnUWcz3_CpRJsQ', 'xjGqlQsEkDeE2VZjHV-JARhywZyaBQ')
r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},
		  auth=auth)
d = r.json()

token = 'bearer ' + d['eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNjk5Mjk4Nzc2LjkxNzcyOCwiaWF0IjoxNjk5MjEyMzc2LjkxNzcyOCwianRpIjoiTHVuQjZOQXA2dWdkUHJjZTA0MlhGeFFCNjc1Qk5RIiwiY2lkIjoiMzlLUmYzRXZMblVXY3ozX0NwUkpzUSIsImxpZCI6InQyX3R5cmdxZ25kIiwiYWlkIjoidDJfdHlyZ3FnbmQiLCJsY2EiOjE2Njc1NjE4MzMwMDAsInNjcCI6ImVKeUtWdEpTaWdVRUFBRF9fd056QVNjIiwiZmxvIjo5fQ.QEa5pT8uQa2Kt2NA8O0whm0_fb6fAM0mSLFfGe0dER7RvVjWYRH1lrWU3XbK-V1FqP_hNqZchNTjTEQcIAGQBsTrsi727G-Z5d4J4HBjunr8b1hH75ESdIEbz4Q4r-S-XAUvWwjtispIXdNqbk-dzLjoBEOxStOk4oluQiCr9-T6D2xkItQHhHjOaE0SeMfuSiFAGH6Adti3byTbO5Zi1uXWRhYA6eA3Tex862u1gPyfOPswEoj51x-oR1P5uc6utOg9Otltifk0wVkyq_U-MLSVsmP7HANk0pg94ZDHsCi8Ztxb9j7hQ6LXWenEzGhDMVLGyC9_ejHN-Bh2QHoHWQ']

base_url = 'https://oauth.reddit.com'

headers = {'Authorization': token}
response = requests.get(base_url + '/api/v1/me', headers=headers)

if response.status_code == 200:
    print(response.json()['name'], response.json()['comment_karma'])

print(r.status_code)

payload = {'q': 'puppies', 'limit': 5, 'sort': 'relevance'}
response = requests.get(api_url + '/subreddits/search', headers=headers, params=payload)
print(response.status_code)
values = response.json()
print(response.text)

for i in range(len(values['data']['children'])):
    print(values['data']['children'][i]['data']['display_name'])
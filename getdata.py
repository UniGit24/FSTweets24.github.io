import requests
app_id = '39KRf3EvLnUWcz3_CpRJsQ'
secret = 'xjGqlQsEkDeE2VZjHV-JARhywZyaBQ'
auth = requests.auth.HTTPBasicAuth(app_id, secret)
reddit_username = 'zbdiss'
reddit_password = 'ucldiss23'
data = {
'grant_type': 'password',
'username': reddit_username,
'password': reddit_password
}
headers = {'User-Agent': 'Tutorial2/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token',
auth=auth, data=data, headers=headers)
res.json()
print(res)
token = res.json()['eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNjk5Mjk4Nzc2LjkxNzcyOCwiaWF0IjoxNjk5MjEyMzc2LjkxNzcyOCwianRpIjoiTHVuQjZOQXA2dWdkUHJjZTA0MlhGeFFCNjc1Qk5RIiwiY2lkIjoiMzlLUmYzRXZMblVXY3ozX0NwUkpzUSIsImxpZCI6InQyX3R5cmdxZ25kIiwiYWlkIjoidDJfdHlyZ3FnbmQiLCJsY2EiOjE2Njc1NjE4MzMwMDAsInNjcCI6ImVKeUtWdEpTaWdVRUFBRF9fd056QVNjIiwiZmxvIjo5fQ.QEa5pT8uQa2Kt2NA8O0whm0_fb6fAM0mSLFfGe0dER7RvVjWYRH1lrWU3XbK-V1FqP_hNqZchNTjTEQcIAGQBsTrsi727G-Z5d4J4HBjunr8b1hH75ESdIEbz4Q4r-S-XAUvWwjtispIXdNqbk-dzLjoBEOxStOk4oluQiCr9-T6D2xkItQHhHjOaE0SeMfuSiFAGH6Adti3byTbO5Zi1uXWRhYA6eA3Tex862u1gPyfOPswEoj51x-oR1P5uc6utOg9Otltifk0wVkyq_U-MLSVsmP7HANk0pg94ZDHsCi8Ztxb9j7hQ6LXWenEzGhDMVLGyC9_ejHN-Bh2QHoHWQ']
headers['Authorization'] = 'bearer {}'.format(token)
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
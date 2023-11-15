import requests
import pandas as pd

def getresults(cityCount):
    df = pd.read_csv('worldcities.csv')
    citylist = df.city

    city = citylist[cityCount]
    eachcity(city, cityCount)

def eachcity(city,cityCount):
    url_string = "http://www.reddit.com/r/"+ city + "/search.json?q=test&count=5&restrict_sr=on"
    #url_string_test = "http://www.reddit.com/r/london/search.json?q=test&count=5&restrict_sr=on"

    # print(url_string)
    url = url_string

    payload = {}
    headers = {
    'Cookie': 'csv=2; edgebucket=CCT4AOhWi82xBMCvv7; loid=0000000000tyrgqgnd.2.1667561833000.Z0FBQUFBQmxSLTI5cXk0dXgxeW9mb0pYbGRpa0JKVXhWNTM5czVsTlJPVWZqY0VsUGpoY1ZubHRCc1J1QUJlX1RFcXdrUlZBcEVnM3JjR21ZNEIxVEJ1WXVNbm5ycWNucmN3MmhwMEd5a0ljMDNkRThrczhHbFVBMTFwcy10eUtHcWJPOUpvay02Z0Y; session_tracker=9UiGWNzRnVokfYK6Si.0.1699212974401.Z0FBQUFBQmxSLTZ2N2wzMFFkMng5M0VrZlNEdHQ1RExyTHVMSFp0NjJmd2tuRWZxY1A0SHRER0NlRE1XRHJlMnY4WUVLNkRTRnJvcDRLbHJkUEFTaXFNNEdnUzVlQnNldTNHbG9ZZUt0YTBIbnFna0d2RHpQNElId2RIYkFnalJuaVJheXhmelhzem0'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    cityCount + 1
    getresults(cityCount)


citycount = 0
getresults(citycount)
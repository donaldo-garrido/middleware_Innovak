def usersCompagination_SABA():

    import requests
    import json

    url = 'https://techsharetest-api.sabacloud.com/v1/people/'

    startPage = 1
    count = 50
    
    payload = {
    "type": "internal",
    "count": count,
    "startPage": startPage,
    }
    
    headers = {'Content-Type':'application/json','SabaCertificate':'VE5CVE5UMTA4XiNeREpBOEtzYTNzU2c0M1NtRU5COEl1a3FsYUdlOFNidzdjUHI2QkRLaUN6S0lSczhBWWM4cHg1TlJ1dkRjU0REeEV2dl81bWhka3k4MzVSTS1mVU5IRkkzVHRndmxoU21jdlE3ekRuU2c1QjRxbXdzMGE0WC1KMDlNT2xZMUE2dVZ0alhIX3Exam9qTUY2Qi1fcnJLaGZB'}
 
    response = requests.get(url, params=payload, headers=headers)
    #print(response)

    

    peopleDict =  response.content.decode("utf-8")
    peopleDict = json.loads(peopleDict)
    totalResults = peopleDict['totalResults']
    print(totalResults)

    totalCalls = int(totalResults/count)+1
    print(totalCalls)


    
    if response.status_code == 200:

        #success_statement = 'Successful {}. Course {} has been completed for user {}'.format(response.status_code, username, externalContentID)
        status = True

        return response.content, status#, success_statement


    else:

        error_statement = 'Error {}'.format(response.status_code)
        status = False

        return response.content, status#, error_statement

usersCompagination_SABA()

def enrollmentsPerson_SABA():

    import requests
    import json
    import pandas as pd

    df = pd.read_csv("username-id.csv")

    backID = df['ID'].to_list()

    enrollsPerson = {}


    for iD in backID:

        url = 'https://techsharetest-api.sabacloud.com/v1/people/'+iD+'/enrollments/search'

        startPage = 1
        count = 3
        
        payload = {
        "count": count,
        "startPage": startPage,
        }
        
        headers = {'Content-Type':'application/json','SabaCertificate':'VE5CVE5UMTA4XiNeREpBOEtzYTNzU2c0M1NtRU5COEl1a3FsYUdlOFNidzdjUHI2QkRLaUN6S0lSczhBWWM4cHg1TlJ1dkRjU0REeEV2dl81bWhka3k4MzVSTS1mVU5IRkkzVHRndmxoU21jdlE3ekRuU2c1QjRxbXdzMGE0WC1KMDlNT2xZMUE2dVZ0alhIX3Exam9qTUY2Qi1fcnJLaGZB'}
    
        response = requests.get(url, params=payload, headers=headers)
        #print(response)

        

        peopleDict =  response.content.decode("utf-8")
        peopleDict = json.loads(peopleDict)
        totalResults = peopleDict['totalResults']
        #print(totalResults)

        enrolls = []

        results = peopleDict['results']
        for result in results:
            enrolls.append(result['id'])

        totalCalls = int(totalResults/count)
        print(totalCalls)

        if totalCalls > 0:
            for call in range(totalCalls):
                payload = {
                "count": count,
                "startPage": startPage+1,
                }
                response = requests.get(url, params=payload, headers=headers)
                
                peopleDict =  response.content.decode("utf-8")
                peopleDict = json.loads(peopleDict)
                results = peopleDict['results']
                for result in results:
                    enrolls.append(result['id'])
        
        if len(enrolls) > 0:
            enrollsPerson.update({iD:enrolls})
            print({iD:enrolls})
        else: pass


        


    print(enrollsPerson)

    return(enrollsPerson)

enrollmentsPerson_SABA()
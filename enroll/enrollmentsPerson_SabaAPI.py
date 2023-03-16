def enrollmentsPerson_SABA():

    import requests
    import json
    import pandas as pd

    df = pd.read_csv("username-id.csv")

    backID = df['ID'].to_list()

    enrollsPerson = {}


    for iD in backID:

        url = 'https://innovaksb-api.sabacloud.com/v1/people/'+iD+'/enrollments/search'

        startPage = 1
        count = 5
        
        payload = {
        "count": count,
        "startPage": startPage,
        }
        
        headers = {'Content-Type':'application/json','SabaCertificate':'TkExVE5CMDE3NF4jXmdiSGd3cUtaVVdLRFZwa3hEQ21UQmZUY3dON1ViUXRZUmQ1eDd2eVp5c3BIWWJZLVQ1SmU0Zk9ES0ZpMmJXUG9jSTRWYVY2Q0RjZ0RodDRzWjVYTUhSNVZzREJxVHBCOG84ZVk2d3FDdk1jWVdzNHNqQktVVmppNTQyR1QyVE9tVVlRdDRnTmk4TDk5ckw1dVR0VVVocWVtd3NVVnBJWkJ4MFVYSWdfSUtrbw'}
    
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
        #print(totalCalls)

        if totalCalls > 0:
            for call in range(totalCalls):
                startPage+=1
                payload = {
                "count": count,
                "startPage": startPage,
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


        

    print('#########################################')
    print(enrollsPerson)
    print('#########################################')

    return(enrollsPerson)



#enrollmentsPerson_SABA()
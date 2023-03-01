def getIDback_SABA():

    import requests
    import json
    import pandas as pd
    import csv

    lst_ID = []

    

    df = pd.read_csv("usernames.csv")

    lst_username = df['USERNAME'].to_list()

    for username in lst_username:


        url = 'https://techsharetest-api.sabacloud.com/v1/people/username='+username+':(id)?'
        
        payload = {
        "type": "internal",
        "searchFields": "id",
        }
        
        headers = {'Content-Type':'application/json','SabaCertificate':'VE5CVE5UMTA4XiNeREpBOEtzYTNzU2c0M1NtRU5COEl1a3FsYUdlOFNidzdjUHI2QkRLaUN6S0lSczhBWWM4cHg1TlJ1dkRjU0REeEV2dl81bWhka3k4MzVSTS1mVU5IRkkzVHRndmxoU21jdlE3ekRuU2c1QjRxbXdzMGE0WC1KMDlNT2xZMUE2dVZ0alhIX3Exam9qTUY2Qi1fcnJLaGZB'}
    
        response = requests.get(url, params=payload, headers=headers)
        #print(response)

        

        peopleDict =  response.content.decode("utf-8")
        peopleDict = json.loads(peopleDict)
        iD = peopleDict['id']
        print(iD)
        lst_ID.append(iD)



        print(response.status_code)

        
    df['ID'] = lst_ID

    print(df)
    

    df.to_csv('./username-id.csv', encoding='utf-8', index=False)
    #print(pd.read_csv('username-id.csv'))

    return(lst_ID)

getIDback_SABA()
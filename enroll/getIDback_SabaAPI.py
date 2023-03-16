def getIDback_SABA():

    import requests
    import json
    import pandas as pd
    import csv

    lst_ID = []

    

    df = pd.read_csv("usernames.csv")

    lst_username = df['USERNAME'].to_list()

    for username in lst_username:


        url = 'https://innovaksb-api.sabacloud.com/v1/people/username='+username+':(id)?'
        
        payload = {
        "type": "internal",
        "searchFields": "id",
        }
        
        headers = {'Content-Type':'application/json','SabaCertificate':'TkExVE5CMDE3NF4jXmdiSGd3cUtaVVdLRFZwa3hEQ21UQmZUY3dON1ViUXRZUmQ1eDd2eVp5c3BIWWJZLVQ1SmU0Zk9ES0ZpMmJXUG9jSTRWYVY2Q0RjZ0RodDRzWjVYTUhSNVZzREJxVHBCOG84ZVk2d3FDdk1jWVdzNHNqQktVVmppNTQyR1QyVE9tVVlRdDRnTmk4TDk5ckw1dVR0VVVocWVtd3NVVnBJWkJ4MFVYSWdfSUtrbw'}
    
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
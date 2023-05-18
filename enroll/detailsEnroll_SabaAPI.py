# Written by Donaldo Garrido
# This code

def detailsEnroll_SABA(id_enroll):

    import requests
    import json
    from datetime import datetime

    today_date = datetime.today().strftime('%d/%m/%Y')


    url = 'https://innovaksb-api.sabacloud.com/v1/enrollments/'+id_enroll+'/sections:regdetail'
    

    
    headers = {'Content-Type':'application/json','SabaCertificate':'TkExVE5CMDE3NF4jXmdiSGd3cUtaVVdLRFZwa3hEQ21UQmZUY3dON1ViUXRZUmQ1eDd2eVp5c3BIWWJZLVQ1SmU0Zk9ES0ZpMmJXUG9jSTRWYVY2Q0RjZ0RodDRzWjVYTUhSNVZzREJxVHBCOG84ZVk2d3FDdk1jWVdzNHNqQktVVmppNTQyR1QyVE9tVVlRdDRnTmk4TDk5ckw1dVR0VVVocWVtd3NVVnBJWkJ4MFVYSWdfSUtrbw'}

    response = requests.get(url, headers=headers)
    print('response status = '+str(response.status_code))

    

    regDict =  response.content.decode("utf-8")
    regDict = json.loads(regDict)
    #print(regDict)
    date_Register = regDict['registrationInfo']['createdOn']['locale']

    if date_Register == today_date:
        
        print(today_date)
        print(date_Register)
        url = 'https://innovaksb-api.sabacloud.com/v1/enrollments/'+id_enroll+'/sections:classdetail'
    
        #headers = {'Content-Type':'application/json','SabaCertificate':'VE5CVE5UMTA4XiNeREpBOEtzYTNzU2c0M1NtRU5COEl1a3FsYUdlOFNidzdjUHI2QkRLaUN6S0lSczhBWWM4cHg1TlJ1dkRjU0REeEV2dl81bWhka3k4MzVSTS1mVU5IRkkzVHRndmxoU21jdlE3ekRuU2c1QjRxbXdzMGE0WC1KMDlNT2xZMUE2dVZ0alhIX3Exam9qTUY2Qi1fcnJLaGZB'}

        response = requests.get(url, headers=headers)

        #print('response status = '+str(response.status_code))

        classDict =  response.content.decode("utf-8")
        classDict = json.loads(classDict)
        class_name = classDict['classDetail']['name']
        print(class_name)

        return class_name

    return False

#print(detailsEnroll_SABA('regdw000000000048988'))
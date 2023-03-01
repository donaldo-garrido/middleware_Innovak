def reportResult_SABA(username, externalContentID, score):

    import requests
    import json

    url = 'https://techsharetest-api.sabacloud.com/v1/partner/reportResult/'
    
    payload = {
    "username": username,
    "vendorName": "Crehana_test",
    "externalContentID": externalContentID,
    "score": score,
    "completionStatus": "completed",
    }
    
    headers = {'Content-Type':'application/json','SabaCertificate':'VE5CVE5UMTA4XiNeREpBOEtzYTNzU2c0M1NtRU5COEl1a3FsYUdlOFNidzdjUHI2QkRLaUN6S0lSczhBWWM4cHg1TlJ1dkRjU0REeEV2dl81bWhka3k4MzVSTS1mVU5IRkkzVHRndmxoU21jdlE3ekRuU2c1QjRxbXdzMGE0WC1KMDlNT2xZMUE2dVZ0alhIX3Exam9qTUY2Qi1fcnJLaGZB'}
 
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    #print(response)
    

    if response.status_code == 200:

        success_statement = 'Successful {}. Course {} has been completed for user {}'.format(response.status_code, username, externalContentID)
        status = True

        return status, success_statement


    else:

        error_statement = 'Error {}'.format(response.status_code)
        status = False

        return status, error_statement

    #print(response.content)

def reportResult_SABA(username, externalContentID, score):

    import requests
    import json

    url = 'https://innovaksb-api.sabacloud.com/v1/partner/reportResult/'
    
    payload = {
    "username": username,
    "vendorName": "Crehana_test",
    "externalContentID": externalContentID,
    "score": score,
    "completionStatus": "passed",
    }
    
    headers = {'Content-Type':'application/json','SabaCertificate':'TkExVE5CMDE3NF4jXmdiSGd3cUtaVVdLRFZwa3hEQ21UQmZUY3dON1ViUXRZUmQ1eDd2eVp5c3BIWWJZLVQ1SmU0Zk9ES0ZpMmJXUG9jSTRWYVY2Q0RjZ0RodDRzWjVYTUhSNVZzREJxVHBCOG84ZVk2d3FDdk1jWVdzNHNqQktVVmppNTQyR1QyVE9tVVlRdDRnTmk4TDk5ckw1dVR0VVVocWVtd3NVVnBJWkJ4MFVYSWdfSUtrbw'}
 
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

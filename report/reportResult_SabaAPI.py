# *******************************************************************
# Written by Donaldo Garrido
# This code let us write in Saba the results of the users taking 
# courses in Crehana with a POST method.
# *******************************************************************

def reportResult_SABA(username, externalContentID, score, slug, certificate_Saba):

    # Import libraries
    import requests
    import json

    # Define the URL (endpoint)
    url = 'https://'+slug+'-api.sabacloud.com/v1/partner/reportResult/'
    
    # Define data and headers
    payload = {
        "username": username,
        "vendorName": "Crehana_test",
        "externalContentID": externalContentID,
        "score": score,
        "completionStatus": "passed",
        }
    
    headers = {'Content-Type':'application/json','SabaCertificate':certificate_Saba}
 
    # API call - POST method
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    # Return different responses depending on whether the call was successful or not 
    if response.status_code == 200:

        success_statement = 'Successful {}. Course {} has been completed for user {}'.format(response.status_code, username, externalContentID)
        status = True

        return status, success_statement

    else:

        error_statement = 'Error {}'.format(response.status_code)
        status = False

        return status, error_statement
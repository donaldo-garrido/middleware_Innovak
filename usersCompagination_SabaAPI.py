# *******************************************************************
# Written by Donaldo Garrido
# This code
# *******************************************************************

def usersCompagination_SABA():

    import requests
    import json
    from info import info_Required


    # May be 'techsharetest', 'innovaksb'
    slug = 'techsharetest'

    certificate_Saba, api_Key, secret_Access = info_Required(slug)

    url = 'https://'+slug+'-api.sabacloud.com/v1/people/'

    startPage = 1
    count = 50
    
    payload = {
    "type": "internal",
    "count": count,
    "startPage": startPage,
    }
    
    headers = {'Content-Type':'application/json','SabaCertificate':certificate_Saba}
 
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

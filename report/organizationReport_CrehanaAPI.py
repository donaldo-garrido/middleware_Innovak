# *******************************************************************
# Written by Donaldo Garrido
# This code has two functions.

# OrganizationReport_CREHANA makes API_calls to obtain all the
# records and its information, such as course_ID or score

# noCalls_CREHANA allows us to know how many calls of the previous
# functions we should do to cover all records taking into account
# pagination.
# *******************************************************************

def organizationReport_CREHANA(offset, size, api_Key, secret_Access):

    # Import libraries
    import requests
    import json

    # URL with the endpoint of Crehana
    url='https://www.crehana.com/api/rest/org/innovak-global/organization_report/'

    # Define headers and arguments for API call
    args = {'offset':offset,'size':size}
    headers = {'Content-Type':'application/json','api-key':api_Key,'secret-access':secret_Access}

    # API call - GET method
    response = requests.get(url, params=args, headers=headers)

    # Convert the response into JSON
    result = response.json()

    # Check if call was succesful
    if response.status_code == 200:

        return result

    else:
        print('Error')


# *******************************************************************
def noCalls_CREHANA(size, api_Key, secret_Access):

    # Import libraries
    import requests
    import json
    import math

    # URL with the endpoint of Crehana
    url='https://www.crehana.com/api/rest/org/innovak-global/organization_report/'

    # Define headers and arguments for API call
    args = {'offset':0,'size':'2'}
    headers = {'Content-Type':'application/json','api-key':api_Key,'secret-access':secret_Access}

    # API call - GET method
    response = requests.get(url, params=args, headers=headers)

    # Convert the response into JSON
    result = response.json()

    # Check how many items we have
    fields = result[0]['fields']

    # Calculate the number of calls needed to cover all items
    no_Calls = math.ceil(fields/size)

    # Check if call was succesful
    if response.status_code == 200:

        return int(no_Calls)

    else:
        print('Error')
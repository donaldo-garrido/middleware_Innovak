# *******************************************************************
# Written by Donaldo Garrido
# This code gets the ID in Saba backend for each user from USERNAME
# *******************************************************************

def getIDback_SABA():

    # Import some libraries
    import requests
    import json
    import pandas as pd
    import csv
    from info import info_Required

    # List to store backends ID
    lst_ID = []

    # Read the list of users we are interested in and convert it to DataFrame
    df = pd.read_csv("usernames.csv") # Write the name of the CSV file

    lst_username = df['USERNAME'].to_list()

    # May be 'techsharetest', 'innovaksb'
    slug = 'innovaksb'

    # Get the certificate
    certificate_Saba, api_Key, secret_Access = info_Required(slug)

    # for to iterate over each user
    for username in lst_username:

        try: 
            # Define URL, payload and headers
            url = 'https://'+slug+'-api.sabacloud.com/v1/people/username='+username+':(id)?'
            
            payload = {
            "type": "internal",
            "searchFields": "id",
            }
            
            headers = {'Content-Type':'application/json','SabaCertificate':certificate_Saba}
        
            # Make API call
            response = requests.get(url, params=payload, headers=headers)
            print(response)

            
            # Decode JSON response and  get the ID
            peopleDict =  response.content.decode("utf-8")
            peopleDict = json.loads(peopleDict)
            iD = peopleDict['id']
            print(iD)

            # Append the ID to list
            lst_ID.append(iD)

        except:
            # If the USERNAME does not exist, indicate it
            lst_ID.append('Not Existing USERNAME')
    
    # Create the column 'ID' in the DataFrame with the obtained IDs
    df['ID'] = lst_ID

    print(df)
    
    # Convert the DataFrame to the final CSV
    df.to_csv('enroll/username-id.csv', encoding='utf-8', index=False)

    return(lst_ID)

getIDback_SABA()
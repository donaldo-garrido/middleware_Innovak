# *******************************************************************
# Written by Donaldo Garrido
# This code is the main pipeline to report results from Crehana to 
# Saba
# *******************************************************************

# Import functions
from organizationReport_CrehanaAPI import organizationReport_CREHANA, noCalls_CREHANA
from reportResult_SabaAPI import reportResult_SABA
from info import info_Required

# Define the slug for the environment selected
# slugs could be 'techsharetest', 'innovaksb'
slug = 'techsharetest'
# Get keys, passwords
certificate_Saba, api_Key, secret_Access = info_Required()

# Define the size of the pagination process
offset = 0
size = 100

# Compute the number of calls to be done
no_Calls = noCalls_CREHANA(size, api_Key, secret_Access)
print('Proceed with {} calls of {} registers each'.format(no_Calls, size))

# Make the calls according to the number obtained in pagination
for call in range(no_Calls):

    # Request to Crehana API
    request_Crehana = organizationReport_CREHANA(offset, size, api_Key, secret_Access)
    print('Offset for this request: {}'.format(offset))

    completion_statement = '\nCourse {} was completed by {}'


    # Iterating through the list of the request response
    for request in request_Crehana:

        # Get relevant values from response dict
        userID = request['user']['id']
        courseID = request['course']['course']['id']
        courseTitle = request['course']['course']['title']
        progress = request['progress']
        certificate = request['course']['has_certificate']
        username = request['user']['user']['email'].split('@')[0].upper()

        # Define the score according to certificate
        if certificate == True:
            score = 100
        elif certificate == False:
            score = 0


        # Check if the course is finished
        if userID == 224861 and progress == 100: # userID condition should be quited

            # Set variables to call SABA API
            username = 'USER-TCSAPI-2' # This should be deleted
            externalContentID = courseID+'-CREHANA'

            # Request to SABA API
            status, statement = reportResult_SABA(username, externalContentID, score, slug, certificate_Saba)


            # Check if the request is succesful
            if status:
                print(statement)

                print(completion_statement.format(courseTitle, username))
            
            else:
                print(statement)

    # Re-define offset to get more records
    offset+=size
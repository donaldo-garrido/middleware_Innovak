from .reportResult_SabaAPI import reportResult_SABA
from .organizationReport_CrehanaAPI import organizationReport_CREHANA


# Request to Crehana API
# Get endpoint "Obtener Progreso de todos los Usuarios"
request_Crehana = organizationReport_CREHANA()

# Type of the request response
print(type(request_Crehana))

completion_statement = '\nCourse {} was completed by {}'


# Iterating through the list of the request response
for request in request_Crehana:
    
    # Get relevant values from response dict
    userID = request['user']['id']
    courseID = request['course']['course']['id']
    courseTitle = request['course']['course']['title']
    progress = request['progress']
    certificate = request['course']['has_certificate']

    if certificate == True:
        score = 100
    elif certificate == False:
        score = 0


    # Check if the course is finished
    if userID == 224861 and progress == 100:
        
        # Set variables to call SABA API
        username = 'USER-TCSAPI-9'
        externalContentID = courseID+'-CREHANA'

        
        # Request to SABA API
        # Get endpoint "partner/reportResult"
        status, statement = reportResult_SABA(username, externalContentID, score)


        # Check if the request is OK
        if status:
            print(statement)

            print(completion_statement.format(courseTitle, username))
        
        else:
            print(statement)
        
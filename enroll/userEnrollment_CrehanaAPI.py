def userEnrollment_CREHANA(user_id, course_id):
    import requests
    import json

    url = 'https://www.crehana.com/api/rest/org/innovak-global/users/'+user_id+'/enrollments/'
    
    payload = {
    "course_id": course_id
    }
    
    #headers = {'Content-Type':'application/json','SabaCertificate':'VE5CVE5UMTA4XiNeREpBOEtzYTNzU2c0M1NtRU5COEl1a3FsYUdlOFNidzdjUHI2QkRLaUN6S0lSczhBWWM4cHg1TlJ1dkRjU0REeEV2dl81bWhka3k4MzVSTS1mVU5IRkkzVHRndmxoU21jdlE3ekRuU2c1QjRxbXdzMGE0WC1KMDlNT2xZMUE2dVZ0alhIX3Exam9qTUY2Qi1fcnJLaGZB'}
    headers = {'api-key':'748801e3479994e76fbb','secret-access':'8730502327095632879f2f56be57cee46680c7ac8411d006a0079195430084c2'}

    response = requests.post(url, data=payload, headers=headers)
    
    statusStatemnt = 'response status = '+str(response.status_code)
    return(response.content, statusStatemnt)
    

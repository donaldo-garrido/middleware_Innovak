def organizationReport_CREHANA():

    import requests
    import json

    url='https://www.crehana.com/api/rest/org/innovak-global/organization_report/'
    args = {'offset':0,'size':'100'}
    headers = {'Content-Type':'application/json','api-key':'748801e3479994e76fbb','secret-access':'8730502327095632879f2f56be57cee46680c7ac8411d006a0079195430084c2'}


    response = requests.get(url, params=args, headers=headers)

    #print(response.content)


    result = response.json()


    if response.status_code == 200:
        #print(response.content)
        #Leer encabezados:

        headers_response = response.headers

        return result

    else:
        print('Error')

#if __name__ == '__main__':
#    get_organization()

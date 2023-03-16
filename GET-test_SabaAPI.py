import requests
import json

def get_organization():
    url='https://techsharetest-api.sabacloud.com/v1/organization'
    args = {'type':'internal','count':'10', 'startPage':'1'}

    #El certificado de SABA es el de Techsharetest
    headers = {'Content-Type':'application/json','SabaCertificate':'VE5CVE5UMTA4XiNeREpBOEtzYTNzU2c0M1NtRU5COEl1a3FsYUdlOFNidzdjUHI2QkRLaUN6S0lSczhBWWM4cHg1TlJ1dkRjU0REeEV2dl81bWhka3k4MzVSTS1mVU5IRkkzVHRndmxoU21jdlE3ekRuU2c1QjRxbXdzMGE0WC1KMDlNT2xZMUE2dVZ0alhIX3Exam9qTUY2Qi1fcnJLaGZB'}


    response = requests.get(url, params=args, headers=headers)

    #print(response.content)
    #json post se encarga de serializarlos
    #data entonces nosotros de serializarlos

    result = response.json()

    print(result)

    if response.status_code == 200:
        #print(response.content)
        #Leer encabezados:

        headers_response = response.headers
        #server = headers_response['server']
        #print(headers_response)
    else:
        print('Error')

if __name__ == '__main__':
    get_organization()

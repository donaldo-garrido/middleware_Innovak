# Written by Donaldo Garrido
# This code has the certificates and api keys for Crehana and Saba API

def info_Required(environment='techsharetest'):
    # Certificates from the environments used

    # The keys from the dictionary are the slugs for each site
    certificates = {'techsharetest': 'VE5CVE5UMTA4XiNeZFNiM2xidFVfWVlOeTd6LWJuNnJWOE5CWnlIN1VNdGZicE9kbzZ6SlZGNmxPT0NBNVFPQzZuSTVWS0kzVXB1RmM5dWZKMjd0MWJtTGJQTzdOenljdmd6RGI2UmpGbV9tenpwVFRfdjBMNEZJQlJVbXhmQmhxNG8zVlJNckp5ZmpYekJVVjJCTDVSNjhiUnNuaHJRUWd3',
                    'innovaksb': 'TkExVE5CMDE3NF4jXnlmQWlZbGNMci1aM0xsclpfLUktM2t5em5WNkYxOUNtR0J6bXp5ZHBudXd5RF92NUQtZW5ucGdHbkhVc0U3VWdsN29BaGFobFBTOXQyZi16UmtpN18zN2lJQXhqX05GZlNNamVWaHNVaW5XZWVYUjVqVmI1aVZsSzRoOXdvOVI1WG42V1pHU2FrRzI0OExGRHNXY1FUNmVsajFybWpKU0F2eHY5cW5lZ1F1VQ',
                    'InnovakPROD': 'We do not have it still'
                    }
    
    # Get the desired certificate
    certificate = certificates[environment]

    # API key and Secret Access of Crehana
    api_Key = '748801e3479994e76fbb'
    secret_Access = '8730502327095632879f2f56be57cee46680c7ac8411d006a0079195430084c2'

    return certificate, api_Key, secret_Access
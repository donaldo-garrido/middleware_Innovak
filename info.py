def info_Required(environment):
    # Certificates from the environments used
    certificates = {'Techsharetest': 'VE5CVE5UMTA4XiNeZFNiM2xidFVfWVlOeTd6LWJuNnJWOE5CWnlIN1VNdGZicE9kbzZ6SlZGNmxPT0NBNVFPQzZuSTVWS0kzVXB1RmM5dWZKMjd0MWJtTGJQTzdOenljdmd6RGI2UmpGbV9tenpwVFRfdjBMNEZJQlJVbXhmQmhxNG8zVlJNckp5ZmpYekJVVjJCTDVSNjhiUnNuaHJRUWd3',
                    'InnovakSB': 'TkExVE5CMDE3NF4jXmdiSGd3cUtaVVdLRFZwa3hEQ21UQmZUY3dON1ViUXRZUmQ1eDd2eVp5c3BIWWJZLVQ1SmU0Zk9ES0ZpMmJXUG9jSTRWYVY2Q0RjZ0RodDRzWjVYTUhSNVZzREJxVHBCOG84ZVk2d3FDdk1jWVdzNHNqQktVVmppNTQyR1QyVE9tVVlRdDRnTmk4TDk5ckw1dVR0VVVocWVtd3NVVnBJWkJ4MFVYSWdfSUtrbw',
                    'InnovakPROD': 'We do not have it still'
                    }
    
    # Get the desired certificate
    certificate = certificates[environment]

    api_Key = '748801e3479994e76fbb'
    secret_Access = '8730502327095632879f2f56be57cee46680c7ac8411d006a0079195430084c2'

    return certificate, api_Key, secret_Access
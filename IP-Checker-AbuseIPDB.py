'''
    1st Oct, 2022
    Mazen Ahmed Gaballah
    ---------------------------
    this is to check bulk of IPs reputation regarding to AbuseIPDB feeds
    Input is a CSV file named 'ips.csv' which containing list of IPs to be searched.
    Output is a CSV file with all information about the IP.
    https://docs.abuseipdb.com
'''

import requests
import json
import csv

# Defining the api-endpoint
API="YOUAPIKEYHERE"
url = 'https://api.abuseipdb.com/api/v2/check'
output=open("results.csv","w",newline='')

with open('ips.csv', encoding="utf-8-sig", mode='r') as ips:
    filewriter = csv.writer(output,delimiter=',',quotechar='|')
    filewriter.writerow(['IPAddress','isPublic','abuseConfidenceScore','countryCode','ISP','usageType','totalReports','numDistinctUsers'])
    ips = csv.reader(ips,delimiter=',')
    for ip in ips:
        ip = ip[0]
        print("Checking IP: {0}".format(ip))
        querystring = {
            'ipAddress': ip,
            'maxAgeInDays': '90'
        }

        headers = {
            'Accept': 'application/json',
            'Key': API
        }

        response = requests.request(method='GET', url=url, headers=headers, params=querystring)

        # Formatted output
        decodedResponse = json.loads(response.text)
        decodedResponse = decodedResponse["data"]
        #print (decodedResponse["ipAddress"])
        filewriter.writerow([decodedResponse["ipAddress"],decodedResponse["isPublic"],decodedResponse["abuseConfidenceScore"],
                             decodedResponse["countryCode"],decodedResponse["isp"],decodedResponse["usageType"],
                             decodedResponse["totalReports"],decodedResponse["numDistinctUsers"]])
        
output.write('\n')
output.close()
print("\nCompleted!\nPlease Check the result file\n")
print("Written By Mazen A. Gaballah")


# <----------------------------------------------------------------------------------------------->
# Use New Alethea to retrieve the list of Currys that are live.

# Explanation:
# Alethea has an API from which you may retrieve useful information. One API call that you may use is to retrieve information regarding Currys. 
# The endpoint is in the following curl call:
# curl -X GET --header 'Accept: application/json' 'http://DOMAIN:8888/metadata/search?aql=SELECT%20hostname,Project,SYSID,Service,TLC%20FROM%20vm%20WHERE%20Product=CURRY%20AND%20Service=TOMCAT%20ORDER%20BY%20SYSID'
# You should create a python program that uses requests library, invoke the above API, retrieve the data and export to a csv file the:
# Project, SYSID, Service, TLC, hostname
# of all Currys.
# Is a field missing in some cases? What are you going to do about it?
# <----------------------------------------------------------------------------------------------->
import requests
import csv

# self explanatory
# !!! Replace the domain accordingly !!! 
api_url="http://DOMAIN:8888/metadata/search?aql=SELECT%20hostname,Project,SYSID,Service,TLC%20FROM%20vm%20WHERE%20Product=CURRY%20AND%20Service=TOMCAT%20ORDER%20BY%20SYSID"

# extracting the JSON (nested) objects under the main "result" object to a list
api_json_response = requests.get(api_url).json()['result']

# creating a new list to append specific JSON objects
# (There is a "resource" object and a "content" object - we wish to extract the "content" JSON object) of api_json_response
# while iterating (for) we now have a dictionary and append accordingly the JSON object we want (both keys and values) to it
final_api_json_response = []
for i in range(len(api_json_response)):
    final_api_json_response.append(api_json_response[i]['content'])

# creating a new file locally and initializing the csv_writer variable to write in that file
output_file=open('C:/Users/k.emmanouilidis/Desktop/python sessions/' + 'flevaris.csv','w',newline='')
csv_writer = csv.writer(output_file)

# defining/ writing the headers of our file which are the JSON keys of our JSON object "content", by creating a list variable "columns"
columns=["Project","SYSID","Service","TLC","hostname"]
csv_writer.writerow(columns)

# using List Comprehension to write the values of the keys into the corresponding columns (json object keys) which were defined earlier
# with this, the tricky part is handled where a "content" JSON object may not include all keys (ie: 1st object is missing the SYSID key and its value)
# Elaborating on the list comprehension: writerow([i.get(col, None) for col in columns]) -> 
# -> get is a python function/method of dictionary data types that extracts the value of a key of a dictionary ie: i.get(the value of the key of 
# final_api_json_response (i) by hardcoding/searching the keys through the columns variable)
# ie: i.get(Project) // next iteration i.get(SYSID) etc. --> get the value of the key of "i" (1st one is "Project" in columns variable) where the key in "i" is "Project".
# // next iteration --> get the value of the key of "i" (2nd one is SYSID in columns variable) where the key in i is SYSID (In this case there is no SYSID key in "i"
# hence it is left null etc.
for i in final_api_json_response:
    csv_writer.writerow([i.get(col, None) for col in columns]) 

# <----------------------------------------------------------------------------------------------->
# Create a database table that holds all information regarding Curry installations.

# Explanation:
# From assignment 3 you had to build an API call towards alethea and retrieve the list of Curry installations that are live. In this assignment you need to extend this program and add a functionality that will store this retrieved information to a Database schema. You will need to:
# Create a new personal table under the db/ schema provided below, with your surname (all small letters), as table name.
# Add the records retrieved from the API call, as fields to the newly created table.
# Extend your previous code with the new functionality. Refactor the previous if needed. Organize your code better. Extra points for those who create easy to maintain/ read code.
# Create two "hardcoded" simple queries. One that requests all the table data and one that requests the data for resource "vm:mdvmsrv1444". Print both results.
# The Database connection details below:
# host: mdvmsrvxxx
# port: x
# username: x
# passwd: x
# database: x
# schema: x

# The table should have the following columns:
# resource, Project, SYSID, Service, TLC, hostname
# <----------------------------------------------------------------------------------------------->
import requests
import psycopg2

# self explanatory
# !!! Replace the domain accordingly !!!
api_url="http://DOMAIN:8888/metadata/search?aql=SELECT%20hostname,Project,SYSID,Service,TLC%20FROM%20vm%20WHERE%20Product=CURRY%20AND%20Service=TOMCAT%20ORDER%20BY%20SYSID"

# Creating 2 lists that contain the JSON keys of the items we want (content & resource):
content_keys = ["Project","SYSID","Service","TLC","hostname"]
resource_keys = ["resource"]

# Function to get specific API data (content & resource)
# Gets the api_url as an argument
def get_api_data(api_url):
    # extracting the JSON (nested) objects under the main "result" object to a list // both content & resource objects
    api_json_response = requests.get(api_url).json()['result']
    # creating a new list to append specific JSON objects
    # (There is a "resource" object and a "content" object - we wish to extract the "content" JSON object) of api_json_response
    json_resource = []
    json_content = []
    # while iterating (for) we now have a dictionary (json_content),
    # a list (json_resource)
    # and append accordingly the JSON object we want (both keys and values) to it
    for i in range(len(api_json_response)):
        json_resource.append(api_json_response[i]['resource'])
        json_content.append(api_json_response[i]['content'])
    return json_resource,json_content

#Function that takes the JSON data of the function get_api_data as arguments and handles:
# 1) the DB connection details
# 2) the creation of the table and the insertion of the JSON data
# 3) SELECT statements and the printing of the results
def db_connection(r,c):
    # connect to the DB
    try:
        connection = psycopg2.connect(user="enterprisedb",
                        password="x",
                        host="x",
                        port="x",
                        database="x")
        cursor = connection.cursor()
        connection.autocommit = True
        # change the table name if needed
        table_name='emmanouilidis'
        # SQL// All queries groupped 
        query_drop_table="DROP TABLE IF EXISTS {}".format(table_name)
        query_create_table="CREATE table public.{} ({} text,{} text,{} text,{} text,{} text, {} text)".format(table_name,*resource_keys,*content_keys)
        query_insert_data="INSERT INTO public.{} VALUES ('{}', '{}','{}','{}','{}','{}')"
        query_select1="SELECT * FROM public.{}".format(table_name)
        query_select2="SELECT * FROM public.{} where resource = 'vm:mdvmsrv1444'".format(table_name)
        # <----------------- Execution of Queries ----------------->
        # DROP table IF EXISTS
        cursor.execute(query_drop_table)
        # CREATE TABLE with the items of the relevant lists (resource_keys, content_keys) as columns
        cursor.execute(query_create_table)
        # Insertion of data to the table, for more info of dict.get refer to assignment 3
        for i in range(len(r)):
            cursor.execute(query_insert_data.format(table_name,r[i],  *[c[i].get(col,None) for col in content_keys]))
        # SQL// SELECT statements and printing
        print("1st select query result (all the table data):")
        cursor.execute(query_select1)
        print(cursor.fetchall())
        print("2nd select query result (all the data for  resource vm:mdvmsrv1444):")
        cursor.execute(query_select2)
        print(cursor.fetchall())
    except Exception as e:
        print(e)
        print("Sth went wrong!")

r,c=get_api_data(api_url)
db_connection(r,c)

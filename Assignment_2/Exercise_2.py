# <----------------------------------------------------------------------------------------------->
# The attached file "wk2_test1_in.csv" is a file with a bunch of rows, each row has comma separated values. 
# Write a program to read this file, then output it to another file "wk2_test1_out.csv" 
# where the fields are also separated by commas but the fields have to be at least 10 characters and at most 15 characters long. 
# (Meaning you have to pad with " " (space) if the field is too short (left justified), or truncate if it is long. 
# (Note: The file is a mess at the end intentionally - How are you going to handle this?)

# For example:
# "dog", "cat"     becomes      "dog       ", "cat       "
# and
# "dog", " abcdefghijklmnopqrs"  become "dog       ", "abcdefghijklmno"
# # <----------------------------------------------------------------------------------------------->
# ********************************************************************************************************************************************
# Status: Re-read the exercise - check if something is missed & assess if there is something else to be done for the last lines
# Notes: Open the output file with notepad++, since Excel seems to automatically truncate the additional spaces (" ") when it comes to numbers.
# ********************************************************************************************************************************************

import csv
list_file = list(csv.reader(open('C:/Users/k.emmanouilidis/Desktop/python sessions/' + 'wk2_test1_in'), delimiter=','))

# ignore
# new_list_file= [[list_file[i][j].replace("\n"," ")] for i in range(len(list_file)) for j in range(len(list_file[i]))]

# Removing \n characters inside each item (string) of the list's "sublists" ie: "Right now a huge\namount"
for i in range(0,len(list_file)):
    list_file[i] = [s.replace("\n"," ") for s in list_file[i]]

# ignore
# new_list=[]

converted_file=open('C:/Users/k.emmanouilidis/Desktop/python sessions/' + 'wk2_test1_out.csv','w')

for i in range(len(list_file)):
    #print(list_file[i]) --- for testing
    for j in range(len(list_file[i])):
        if len(list_file[i][j])>15:
            x=(list_file[i][j][:15])
            #print(x)
            converted_file.write(x +',')
        if len(list_file[i][j])<10:
            x= (list_file[i][j] + ((10-len(list_file[i][j]))*' '))
            #print(x)
            converted_file.write(x +',')
        if (len(list_file[i][j])>=10 and len(list_file[i][j])<=15):
            x=list_file[i][j]
            #print(x)
            converted_file.write(x +',')
    created_file.write('\n')
created_file.close()

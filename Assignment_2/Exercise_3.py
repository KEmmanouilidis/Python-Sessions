# <-------------------------------------------------------------------------------------------------------------------------------------------->
# The attached file "wk2_test2_in.zip" is the JBOSS GC (Garbage Collection) log for the period of the observed outage. (Zipped)
# The file is of the following format:
# 2018-05-11T06:12:44.646+0000: 4.267: [GC 440402K->4512K(13762560K), 0.0143860 secs]
# 2018-05-11T06:12:44.660+0000: 4.281: [Full GC 4512K->4280K(13762560K), 0.1075070 secs]
# 2018-05-11T06:13:11.485+0000: 31.106: [GC 5509304K->45427K(13762560K), 0.0565090 secs]
# 2018-05-11T06:14:02.008+0000: 81.629: [GC 5550451K->145104K(13762560K), 0.2085120 secs]
# 2018-05-29T15:36:57.935+0000: 1589057.556: [Full GC 2364371K->1153191K(14424896K), 3secs]
                
# Part 1:  (hard)
# Write a program that outputs:

# (1) The period (time range) that is covered by this log.
# (2) Number of minor GCs.
# (3) Number of full GCs.

# Part 2:  (harder yet)
# Write a program that calculates the average time a minor and full GC takes, and outputs:

# (1) Average time for a minor GC.
# (2) Average time for a Full GC.
# (3) The 3 top minor GCs that took the longest and the same for Full GCs, with the amount of time they took and the time when they occurred.
# <-------------------------------------------------------------------------------------------------------------------------------------------->

import csv

list_file = list(csv.reader(open('C:/Users/k.emmanouilidis/Desktop/python sessions/' + 'wk2_test2_in.log'), delimiter=','))
# new_list_file= [[list_file[i][j].replace("\n"," ")] for i in range(len(list_file)) for j in range(len(list_file[i]))]

fgc=[]
mgc=[]
fgc_ts=[]
mgc_ts=[]
fgc_count=0
mgc_count=0
all_gc=[]

for i in range(len(list_file)):
    all_gc.append(list_file[i][0][:28]) 
    all_gc[i]=all_gc[i].replace("T"," ") # Remove the "T" from the datetime/timestamp
    if 'Full GC' in list_file[i][0]:
        fgc.append(list_file[i][1][1:10]) # append the duration value / Full GC
        fgc_ts.append(all_gc[i][0:28])  # append the timestamp value / Full FC
        fgc_count+=1 # Full GC count
    elif 'Full GC' not in list_file[i][0] and 'GC' in list_file[i][0]:
        mgc.append(list_file[i][1][1:10]) # append the duration value / Minor GC
        mgc_ts.append(all_gc[i][0:28]) ## append the duration value / Minor GC
        mgc_count+=1 # Minor GC count


for i in range(len(fgc)):
    fgc[i]=float(fgc[i])
for i in range(len(mgc)):
    mgc[i]=float(mgc[i])

top3fgc=(sorted(zip(fgc, fgc_ts), reverse=True)[0:3])
top3mgc=(sorted(zip(mgc, mgc_ts), reverse=True)[0:3])


print("-> The period (time range) of the log file is between {} and {}. \
\n-> The number of minor GCs is: {} \
\n-> The number of full GCs is: {}  \
\n-> The average time for a Full GC is {}: \
\n-> The average time for a minor GC is {}: ".format(min(all_gc),max(all_gc),mgc_count,fgc_count,sum(fgc) / len(fgc),sum(mgc) / len(mgc)))

print("-> The top 3 Full GCs in duration along with their timestamps are:")
for i in range(len(top3fgc)):
    print("   {}). {} & duration:{}".format(i+1,top3fgc[i][1],top3fgc[i][0]))

print("-> The top 3 minor GCs in duration along with their timestamps are:")
for i in range(len(top3mgc)):
    print("   {}). {} & duration:{}".format(i+1,top3mgc[i][1],top3mgc[i][0]))

# Notes:
# Re-visit all exercises of assignment 2. 
# All need rework (better readability, better use of functions, classes, imports (ie import exercise 1 & use it to exercise 3 etc.))
# Many for/ifs, too many variables, probably confusing code structure etc.
# Ideas noted VS implementation (?)

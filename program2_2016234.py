import time

start_time = time.time()

metadata =open('metadata_2016234.txt','r')

final_metadata=[]

for line in metadata:
	line=line[:-1] #Removes the trailing \n
	mylist=line.split()
	final_metadata.append(mylist)
# print final_metadata
metadata.close()

Data_final=[]

sample_file =open('Db_2016234','r')
for line in sample_file:
	line=line[:-1] #Removes the trailing \n
	mylist=line.split(",")
	Data={}
	for i in range(0,len(final_metadata)):
		Data[final_metadata[i][0]]=mylist[i]
	Data_final.append(Data)
	
# print Data_final

#OUTCOME 1
# Printing the data in the file in the same format
print "\nOUTCOME1 : Printing the data in the Database\n"
for item in Data_final:
	i=0
	for i in range(0,len(final_metadata)):
		if(final_metadata[i][1]=="C"):
			print item[final_metadata[i][0]]+",",
		else:
			print str(item[final_metadata[i][0]])+",",
	print ""

#OUTCOME 2

for i in range(0,len(final_metadata)):
	if(final_metadata[i][1]=="I"):
		final_metadata[i].append(0)
	else:
		final_metadata[i].append(-1)

for item in Data_final:
	for i in range(0,len(final_metadata)):
		if(final_metadata[i][len(final_metadata[i])-1]>=0):
			final_metadata[i][len(final_metadata[i])-1]=int(final_metadata[i][len(final_metadata[i])-1])+int(item[final_metadata[i][0]])

print ""

print 'OUTCOME2: Printing the Sums of the various fields\n'
for i in range(0,len(final_metadata)):
	if(final_metadata[i][len(final_metadata[i])-1]==-1):
		print final_metadata[i][0]+' '+'Non-Numeric Field'
	else:
		print final_metadata[i][0]+' '+str(final_metadata[i][len(final_metadata[i])-1])
print ""

print "Execution time : --- %s seconds ---\n" % (time.time() - start_time)

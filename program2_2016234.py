import time

start_time = time.time()

metadata =open('metadata_2016234.txt','r')

final_metadata=[]

for line in metadata:
	line=line[:-1] #Removes the trailing \n
	mylist=line.split()
	final_metadata.append(mylist)
	# print mylist
# print final_metadata
metadata.close()

Data_final=[]
mylist=[]

#print final_metadata[2][2]

sample_file =open('Db_2016234','r')
for line in sample_file:
	line=line.replace("'","") #Removes the extra 's
	arr=list(line)
	arr=arr[:-1] #Removes the trailing \n
	a=""
	counter_size=0
	Data={}
	for i in range(0,len(final_metadata)):
		size=int(final_metadata[i][2])
		a=""
		while(counter_size<len(arr) and arr[counter_size]!=','):
			a+=str(arr[counter_size])
			counter_size+=1
		counter_size+=1
		Data[final_metadata[i][0]]=a
	Data_final.append(Data)
#print Data_final

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

name = raw_input()

print 'OUTCOME2: Printing the Sums of the given field '+name+':\n'
for i in range(0,len(final_metadata)):
	if(final_metadata[i][0]==name):
		if(final_metadata[i][len(final_metadata[i])-1]==-1):
			print 'Non-Numeric Field'
		else:
			print str(final_metadata[i][len(final_metadata[i])-1])
print ""
# print final_metadata

print "Execution time : --- %s seconds ---\n" % (time.time() - start_time)

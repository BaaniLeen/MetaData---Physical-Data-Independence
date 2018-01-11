import time

start_time = time.time()

#sample_file =open('Db_2016234','r')
sample_file =open('Db_2016234','r')

Data_final=[]

for line in sample_file:
	line=line[:-1] #Removes the trailing \n
	mylist=line.split(",")
	# print mylist
	Data={}
	Data['Name']=mylist[0]
	Data['Roll_No'] = mylist[1]
	Data['Outside_Delhi_Status']=mylist[2]
	Data_final.append(Data)
	# print Data

#Printing the data with the labels in the form of a dictionary - Can be further used for processing data
# print Data_final

#OUTCOME 1
# Printing the data in the file in the same format
print "\nOUTCOME1 : Printing the data in the Database\n"
for item in Data_final:
	print item['Name']+","+item['Roll_No']+"'"+item['Outside_Delhi_Status']

#OUTCOME 2
count_rollno=0
for item in Data_final:
	count_rollno=count_rollno+int(item['Roll_No'])

print ""

print 'OUTCOME2: Printing the Sums of the various fields\n'
print 'Name'+' '+'Non-Numeric Field'
print 'Roll_No'+" "+str(count_rollno)
print 'Outside_Delhi_Status'+' '+'Non-Numeric Field'

print ""

print "Execution time : --- %s seconds ---\n" % (time.time() - start_time)

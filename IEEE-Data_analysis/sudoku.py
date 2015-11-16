import random
import sys
def readsud():
	readopen=open("input.txt","w")
	for i in range(1,17):
		print "Enter element : "
		num=raw_input("<")
		readopen.write(num)
		if i%4==0:
			readopen.write("\n")
	readopen.close()


def displaysud():
	fopen=open("input.txt","r")
	data=fopen.read()
	list1=list(data)
	for i in range(0,16):
		print list1[i],
		if((i+1)%4==0):
			print " "


	fopen.close()

def check(temp,name,i,j):
	list1=list(temp)
	k=0
	count=0
	while k<4:
		if list1[4*i+k]==name:
			count=count+1
		k=k+1
	#print count
	if count>0:
		return 0
	k=0
	count=0
	while k<4:
		if list1[4*k+j]==name:
			count=count+1
		k=k+1
	if count>0:
		return 0
	
	count=0
	if i<2 and j<2:
		for k in range(2):
			for l in range(2):
				if list1[4*k+l]==name:
					count=count+1	
	
	if count>0:
		return 0
	
	count=0
	if i>=2 and j<2 :
		for k in range(2,4):
			for l in range(2):
				if list1[4*k+l]==name :
					count=count+1	
	if count>0:
		return 0

	count=0
	if i<2 and j>=2 :
		for k in range(2):
			for l in range(2,4):
				if list1[4*k+l]==name :
					count=count+1	
	if count>0:
		return 0

	count=0
	if i>=2 and j>=2:
		for k in range(2,4):
			for l in range(2,4):
				if list1[4*k+l]==name :
					count=count+1	
	
	if count>0:
		return 0

	return 1


fopen=open("input.txt","r")
r=random.randint(0,5)
for i in range(r):
	data1=fopen.readline()
data1=fopen.readline()
list2=list(data1)
for i in range(16):
	print list2[i],
	if((i+1)%4==0):
		print " "

i=0
while i<4:
	j=0
	while j<4:
		fout=open("output.txt","w")
		list1=list(data1)
		if list1[(4*i)+j]=='0' :
			print "Enter the Number at Coordinate(%d,%d) : "%(i+1,j+1)
			inp=raw_input(">")
			if inp=='1' or inp=='2' or inp=='3' or inp=='4':
				if check(data1,'1',i,j)==1 or check(data1,'2',i,j)==1 or check(data1,'3',i,j)==1 or check(data1,'4',i,j)==1 :
					if check(data1,inp,i,j)==1 :
						list1[4*i+j]=inp
						data1="".join(list1)
						fout.truncate()
						fout.write(data1)
						fout.close()
						print list1
					else:
						print "not allowed ..\nInput again"
						j=j-1
				else:
					print "Wrong Approach..\nBetter Luck next time"
					sys.exit()
				
			else:
				print "Not Possible\nInput Again....."
				j=j-1
		j=j+1
	i=i+1
fout=open("output.txt","r")
data2=fout.read()
list2=list(data2)
for i in range(16):
	print list2[i],
	if((i+1)%4==0):
		print " "

fout.close()
fopen.close()


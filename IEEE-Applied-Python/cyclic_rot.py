from itertools import permutations
def is_cyclic_rotation(a,b):
	b=b*2
	flag=1
	for j in range(0,len(b)):
		if a[0]==b[j]:
			k=0
			while k<len(a) and j+k<len(b):
				if a[k]!=b[j+k]:
					flag=0
					break
				k=k+1
			if(flag==0):
				break
			else:
				return True	
	if flag==0:
		return False

str1=raw_input("Enter the First string ")
sr2=raw_input("Enter the Second String ")
if is_cyclic_rotation(str1,sr2)==True:
	print " Is a Cyclic Rotation"
else:
	print "Not a Cyclic Rotation"

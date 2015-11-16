def xorstrings(x1,x2):
	list1=[]
	for i in range(0,len(x1)):
		temp1=int(x1[i],16)^int(x2[i],16) #converting hex to int
		temp1='{:x}'.format(temp1)#converting the result into hex 
		list1.append(temp1)#appending the hex final into the list
	return list1

str1=raw_input("Enter the string 1 ")
str2=raw_input("Enter the string 2 ")
list2=xorstrings(str1,str2)
list2="".join(list2)
print list2


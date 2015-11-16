import base64

def xorstrings(x1,x2):
	list1=[]
	for i in xrange(0,len(x1)):
		temp=chr(ord(x1[i])^ord(x2[i%len(x2)]))
		list1.append(temp)
	list1="".join(list1)
	return list1


str1=raw_input()
str2=raw_input()

str1=str1.decode('hex')
str2=str2.decode('hex')

ans=xorstrings(str1,str2)

print "The given strings after XOR : " + ans.encode('hex')

from itertools import permutations
import sys
def is_anagram(str1,str2):
	a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	b=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	for i in range(0,len(str1)):
		temp1=ord(str1[i]) #ASCII Values of the character
		temp2=ord('a')
		a[temp1-temp2]=a[temp1-temp2]+1 #increasing the number of that character in the string
	for i in range(0,len(str2)):
		temp1=ord(str2[i])
		temp2=ord('a')
		b[temp1-temp2]=b[temp1-temp2]+1
	for i in range(0,26):
		if a[i]!=b[i]:
			return 0
	return 1


str1=raw_input("Enter the string 1 : ")
str2=raw_input("Enter the string 2 : ")
if is_anagram(str1,str2)==1:
	print "string %s and string %s are anagrams"%(str1,str2)
else:
	print "string %s and string %s are not anagrams"%(str1,str2)


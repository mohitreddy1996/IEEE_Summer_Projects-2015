#function for insertion sort
def insertion_sort(arr):
	for i in range(1,len(arr)):
		j=i
		while j>0 and arr[j-1]>arr[j]:
			temp=arr[j] #swapping 
			arr[j]=arr[j-1]
			arr[j-1]=temp
			j=j-1
	for i in range(0,len(arr)):
		print "%d"%arr[i],


data=raw_input("Enter the array to be sorted : ")
data=data.split(' ')
#converting all the character into integer
for i in range(0,len(data)):
	data[i]=int(data[i])
	#print data,
print "Array to be sorted: "
insertion_sort(data)

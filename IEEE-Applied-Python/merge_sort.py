import sys
def merge(a,p,q,r):
	n1=q-p+1
	n2=r-q
	L=[0]*(n1)
	R=[0]*(n2)
	for i in range(0,n1):
		L[i]=a[p+i]
	L.append(sys.maxint)
	for i in range(0,n2):
		R[i]=a[q+i+1]
	R.append(sys.maxint)
	w=0
	e=0
	for i in range(p,r+1):
		if L[w]<R[e]:
			a[i]=L[w]
			w=w+1
		else:
			a[i]=R[e]
			e=e+1			


def mergesort(a,p,r):
	if p<r:
		q=(p+r)/2
		mergesort(a,p,q)
		mergesort(a,q+1,r)
		merge(a,p,q,r)


data1=raw_input("Enter the array ")
data1=data1.split(' ')
len1=len(data1)
for i in range(0,len1):
	data1[i]=int(data1[i])
mergesort(data1,0,len1-1)
print data1

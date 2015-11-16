def fibo(m):
			if m==1:
				return 0
			elif m==2:
				return 1
			else:
				return fibo(m-1)+fibo(m-2)
def even_fibo_sum(n):
	m=1
	sum=0
	while fibo(m)<=n:
		if fibo(m)%2==0:
			sum=sum+fibo(m)
		m=m+1
	return sum	
		
		

num=raw_input("Enter the number ")
num=int(num)
sum=even_fibo_sum(num)
print "Sum of all even numbers in the fibonacci series till %d is %d"%(num,sum)
		
	

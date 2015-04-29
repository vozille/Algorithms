def decimal_to_base_x(n,x):
	base_x = 0
	i = 1
	while n > 0:
		r = n%x
		n = n/x
		base_x += r*i
		i = i*10
	return base_x

def fact(n):
	return 0**n or n*fact(n-1)

def nCr(n,r):
	return fact(n)/(fact(n-r)*fact(r))

def Lucas_nCr(n,r,m):	# m is prime
	n1 = str(decimal_to_base_x(n,m))
	r1 = str(decimal_to_base_x(r,m))
	r1 = '0'*(len(n1)-len(r1))+r1
	n1 = map(int,n1)
	r1 = map(int,r1)
	ans = 0
	for i in range(len(n1)):
		ans += nCr(n1[i],r1[i])
	return ans%m

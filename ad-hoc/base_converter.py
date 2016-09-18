# I am so stupid, i just keep forgetting this once a while
def decimal_to_base_x(n,x):
	base_x = 0
	i = 1
	while n > 0:
		r = n%x
		n = n/x
		base_x += r*i
		i = i*10
	return base_x
def base_x_to_decimal(n,x):
	base_10 = 0
	i = 0
	while n > 0:
		r = n%10
		n = n/10
		base_10 += x**i
		i += 1
	return base_10

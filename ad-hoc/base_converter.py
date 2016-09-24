# I am so stupid, i just keep forgetting this once a while
# for base < 10
def decimal_to_base_x(num, base):
	base_x = 0
	i = 1
	while num > 0:
		r = num% base
		num = num/ base
		base_x += r*i
		i = i*10
	return base_x
def base_x_to_decimal(num, base):
	base_10 = 0
	i = 0
	while num > 0:
		r = num%10
		num = num/10
		base_10 +=  base**i
		i += 1
	return base_10


print decimal_to_base_x(5, 2)


print(hex(3)+'.',end='')
max_n = 1000

for n in range(max_n):

	summation = 0.0

	for k in range(n+1):

		summation += (
			4*(16**(n-k)%(8*k+1))/(8*k+1)
			- 2*(16**(n-k)%(8*k+4))/(8*k+4)
			- (16**(n-k)%(8*k+5))/(8*k+5)
			- (16**(n-k)%(8*k+6))/(8*k+6)
		)

	d = str(summation).split('.')[1]

	d = hex(round(16*float('0.'+d)))[-1]

	print(d,end='',flush=True)

print()

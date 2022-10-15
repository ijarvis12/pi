#!/usr/bin/env python3

import torch

n = input("Input hex digit n to find: ")

try:
	n = int(n)
except:
	print("Could not interpret input as integer.")
	_ = input("Press <Enter> to end program")
	exit()

cpu = torch.device('cpu')
cuda = torch.device('cuda')

with torch.cuda.device():
	
	summation = torch.tensor(0.0, device=cuda)
	
	for k in range(n+1):
		
		nk = torch.tensor(16**(n-k), device=cuda)
		k1 = torch.tensor(8*k+1, device=cuda)
		k4 = torch.tensor(8*k+4, device=cuda)
		k5 = torch.tensor(8*k+5, device=cuda)
		k6 = torch.tensor(8*k+6, device=cuda)
		
		summation += (
				4*(nk % k1) / k1
				- 2*(nk % k4) / k4
				- (nk % k5) / k5
				- (nk % k6) / k6
		)
	
#   send var to cpu for displaying
	summ = summation.to(device=cpu)
	
digit = str(summ.item()).split('.')[1]

digit = hex(round(16*float('0.'+digit)))[-1]

print()
print(digit)
print()

_ = input("Press <Enter> to end program.")

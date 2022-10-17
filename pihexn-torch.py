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

# use gpu
with torch.cuda.device(cuda):
	
#	initialization
	i = torch.tensor(n).cuda()
	summation = torch.tensor(0.0, device=cuda)
	nk = torch.tensor(0, device=cuda)
	k1 = torch.tensor(0, device=cuda)
	k4 = torch.tensor(0, device=cuda)
	k5 = torch.tensor(0, device=cuda)
	k6 = torch.tensor(0, device=cuda)
	j = i.item()
	
#	do grunt work
	for k in range(j+1):
		
		nk = 16**(j-k)
		k1 = 8*k+1
		k4 = 8*k+4
		k5 = 8*k+5
		k6 = 8*k+6
		
		summation += (
				4*(nk % k1) / k1
				- 2*(nk % k4) / k4
				- (nk % k5) / k5
				- (nk % k6) / k6
		)
	
#	send var to cpu for displaying
	summation.to(device=cpu)
	
digit = str(summation.item()).split('.')[1]

digit = hex(round(16*float('0.'+digit)))[-1]

print()
print(digit)
print()

_ = input("Press <Enter> to end program.")

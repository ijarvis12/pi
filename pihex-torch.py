#!/usr/bin/env python3

import torch

cpu = torch.device('cpu')
cuda = torch.device('cuda')

print('3',end='')
max_n = 1000

for n in range(max_n):
	
#	use gpu
	with torch.cuda.device(cuda):
		
#		initialize
		i = torch.tensor(n).cuda()
		summation = torch.tensor(0.0, device=cuda)
		nk = torch.tensor(0, device=cuda)
		k1 = torch.tensor(0, device=cuda)
		k4 = torch.tensor(0, device=cuda)
		k5 = torch.tensor(0, device=cuda)
		k6 = torch.tensor(0, device=cuda)
		j = i.item()
		
#		do grunt work
		iterations = j + 1
		for k in range(iterations):
			
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
		
#		send var to cpu for displaying
		summation.to(device=cpu)
		
	digit = str(summation.item()).split('.')[1]
	
	digit = hex(round(16*float('0.'+digit)))[-1]
	
	print(digit,end='',flush=True)

print()
_ = input("Press <Enter> to end program.")

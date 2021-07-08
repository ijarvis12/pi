from decimal import Decimal, getcontext
from time import time

# set decimal precision
getcontext().prec = 1750

# get starting time for runtime total
time1 = time()

# initialize constants
pi = Decimal(0)
one = Decimal(1)
four = Decimal(4)
two = Decimal(2)

# do calculation
for k in range(0,1447):
        pi += (one/16**k)*(four/(8*k+1)-two/(8*k+4)-one/(8*k+5)-one/(8*k+6))

# get ending time for runtime total
time2 = time()

print(pi)
print('Total calculation time: ', time2-time1)

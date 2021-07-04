from decimal import Decimal, getcontext
from time import time

getcontext().prec = 1750

time1 = time()

pi = Decimal(0)
one = Decimal(1)
four = Decimal(4)
two = Decimal(2)

for k in range(0,1447):
        pi += (one/16**k)*(four/(8*k+1)-two/(8*k+4)-one/(8*k+5)-one/(8*k+6))

time2 = time()

print(pi)
print('Total calculation time: ', time2-time1)

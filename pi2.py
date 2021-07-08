# function pi finds the digits of pi given inputs
# inputs: numprocs: number of processes running the function
#                p: process number
#              con: context precision
#              end: ending summation iteration 
#      return_list: dictionary of return values
def pi(numprocs,p,con,end,return_list):
    from decimal import Decimal, getcontext
        
#   variable start is the starting point to search from
    start = end*p//numprocs
    if start < 2:
    start = 2

#   do the grunt work
    getcontext.prec = con
    pi = Decimal(0)
    one = Decimal(1)
    four = Decimal(4)
    two = Decimal(2)
    for k in range(start,end+1):
        pi += (one/16**k)*(four/(8*k+1)-two/(8*k+4)-one/(8*k+5)-one/(8*k+6))
    
    return_list.append(pi)
    

##                                                        ##
## main process that spawns jobs for finding digits of pi ##
##                                                        ##
if __name__ == '__main__':

    import multiprocessing
    from decimal import Decimal, getcontext
    from time import time

#   number of processes the computer has
    numprocs = multiprocessing.cpu_count()
    
#   get starting time for runtime total
    time1 = time()
    
#   multiprocessing jobs
    jobs = []
        
#   shared list between processes
    return_list = multiprocessing.Manager().list()
    
#   set pi digit precision
    con = getcontext.prec = 1750
    
#   start jobs
    for p in range(numprocs):
        job = multiprocessing.Process(target=primes, args=(numprocs,p,con,1447,return_list,))
        jobs.append(job)
        job.start()

#   wait for jobs to finish
    for job in jobs:
        job.join()
    
#   sum all the subprocesses digits to get pi
    pi = Decimal(0)
    for p in return_list:
        pi += p
    
#   get ending time for runtime total
    time2 = time()

    print(pi)
    print('Total calculation time: ', time2-time1)

    garbage = input("Press <Enter> to end program")

# function pi finds the digits of pi given inputs
# inputs: num_procs: number of processes running the function
#                 p: process number
#              prec: context precision
#          iter_tot: summation iteration total 
#       return_list: list of return values
def pi(num_procs,p,prec,iter_tot,return_list):
    from decimal import Decimal, getcontext
        
#   variable start is the starting point
    start = iter_tot*p//num_procs
    
#   variable end is the stopping point
    end = iter_tot*(p+1)//num_procs

#   setup
    getcontext().prec = prec
    pi = Decimal(0)
    one = Decimal(1)
    four = Decimal(4)
    two = Decimal(2)
    
#   do the grunt work
    for k in range(start,end):
        pi += (one/16**k)*(four/(8*k+1)-two/(8*k+4)-one/(8*k+5)-one/(8*k+6))
    
    return_list.append(pi)
    return
    

##                                                        ##
## main process that spawns jobs for finding digits of pi ##
##                                                        ##
if __name__ == '__main__':

    import multiprocessing
    from decimal import Decimal, getcontext
    from time import time

#   number of processes the computer has
    num_procs = multiprocessing.cpu_count()
    
#   get starting time for runtime total
    time1 = time()
    
#   multiprocessing jobs
    jobs = []
        
#   shared list between processes
    return_list = multiprocessing.Manager().list()
    
#   set pi digit precision
    prec = getcontext().prec = 1750
    
#   start jobs
    for p in range(num_procs):
        job = multiprocessing.Process(target=pi, args=(num_procs,p,prec,1448,return_list,))
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

    _ = input("Press <Enter> to end program")

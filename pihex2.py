# function pi finds the hex digit of pi given inputs
# inputs: num_procs: number of processes running the function
#                 p: process number
#                 n: hex digit number 
#       sum_list: list of return values
def pi(num_procs,p,n,sum_list):
        
#   variable start is the starting point
    start = n*p//num_procs
    
#   variable end is the stopping point
    end = n*(p+1)//num_procs
    
#   do the grunt work
    partial_dig = 0.0
    for k in range(start,end):
        partial_dig += (
                        4*(16**(n-k)%(8*k+1))/(8*k+1)
                        - 2*(16**(n-k)%(8*k+4))/(8*k+4)
                        - (16**(n-k)%(8*k+5))/(8*k+5)
                        - (16**(n-k)%(8*k+6))/(8*k+6)
        )
    
    sum_list.append(partial_dig)
    

##                                                            ##
## main process that spawns jobs for finding hex digits of pi ##
##                                                            ##
if __name__ == '__main__':

    import multiprocessing
    from time import time

#   number of processes the computer has
    num_procs = multiprocessing.cpu_count()
    
#   get starting time for runtime total
    time1 = time()
    
#   inital setup
    print(hex(3)+'.'+'ec419b778663f93d',end='')
    max_n = 1000
    
#   bulk work, find each hex digit n up to max_n
    for n in range(16,max_n):    
        
#       multiprocessing jobs
        jobs = []
        
#       shared list between processes
        sum_list = multiprocessing.Manager().list()
        
#       start jobs
        for p in range(num_procs):
            job = multiprocessing.Process(target=pi, args=(num_procs,p,n,sum_list,))
            jobs.append(job)
            job.start()
        
#       wait for jobs to finish
        for job in jobs:
            job.join()
        
#       put the sum together to get the hex digit of pi
        summation = 0.0
        for s in sum_list:
            summation += s
        
#       and the last point
        k = n
        summation += (
                        4*(16**(n-k)%(8*k+1))/(8*k+1)
                        - 2*(16**(n-k)%(8*k+4))/(8*k+4)
                        - (16**(n-k)%(8*k+5))/(8*k+5)
                        - (16**(n-k)%(8*k+6))/(8*k+6)
        )
        
#       finishing touches
        digit = str(summation).split('.')[1]
        digit = hex(round(16*float('0.'+digit)))[-1]
        
#       print the hex digit of pi!
        print(digit,end='',flush=True)
    
#   get ending time for runtime total
    time2 = time()

    print()
    print('Total calculation time: ', time2-time1)

    _ = input("Press <Enter> to end program")

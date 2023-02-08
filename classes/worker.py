""" -----| THEIA WORKER CLASS 
This is what defines the individual behavior of each 
of the workers that inhabit the threadpool.
"""
import random, time 

class TheiaWorker: 
    def __init__(self, threadpool, id_num, status):
        self.threadpool = threadpool
        self.id_num = id_num 
        self.status = status 
    
    def __str__(self): 
        return((f"  ↳ Worker {self.id_num}").ljust(30, ".") + 
            (f"{self.status}").rjust(29, ".") + " ")
    

""" -----| THEIA WORKER BEHAVIOR 
These are the functions that the workers 
actually inact. Idk, I'm fat and retarded bro.
"""
def test_function(worker):
    test_status = [ 
        "Getting selenium", 
        "Finding victim", 
        "Logging into account"
    ]

    while True: 
        time.sleep(random.randint(0, 2))
        worker.status = test_status[random.randint(0, 2)]
   
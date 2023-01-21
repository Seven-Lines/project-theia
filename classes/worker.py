""" -----| THEIA WORKER CLASS 
This is what defines the individual behavior of each 
of the workers that inhabit the threadpool.
"""
import random 
from termcolor import colored  

class TheiaWorker: 
    def __init__(self, threadpool, id_num, status):
        self.threadpool = threadpool
        self.id_num = id_num 
        self.status = status 
    
    def __str__(self): 
        self.setRandomStatus()
        return((f"  ↳ Worker {self.id_num}").ljust(30, ".") + 
            (f"{self.status}").rjust(29, ".") + " ")

    def setRandomStatus(self):
        test_status = [ 
            "Getting selenium", 
            "Finding victim", 
            "Logging into count"
        ]
        self.status = test_status[random.randint(0, 2)]


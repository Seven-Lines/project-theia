""" -----| THREAD POOL EXECUTOR CLASS
Allows for the creation of multiple different uses of the bots 
while keeping the program running at all times. This feature allows 
me to focus the efforts of the bots, even as the program runs 24/7. 
On a whim I can change the focus of the bots from reconnaissance to 
targeting one of my videos. 
"""
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored  
import random 

from classes.worker import TheiaWorker
from classes.worker import test_function

class workerpool: 
    def __init__(self, id, task, mw): 
        self.id = id
        self.executor = ThreadPoolExecutor(max_workers=mw) 
        self.workers = []; [self.workers.append(TheiaWorker(self.executor, (num+1), "")) for num in range(mw)]  
        match task: 
            case "1": # TESTING THREADING
                self.task = "Test\Threading"
                with self.executor as executor:
                    executor.map(test_function, self.workers) # function, workers 
                
    def __str__(self): 
        return(f"[WorkerPool {self.id} - {self.task}]")
    def __del__(self):
        print(f"I am deleting {self.id}")
        #self.workerpool.shutdown(wait=False)

    def getId(self): return(self.id)
    def getWorkers(self): return(self.workers)
    def getworkerpool(self): return(self.executor) 
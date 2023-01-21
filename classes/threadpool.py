""" -----| THREAD POOL EXECUTOR CLASS
Allows for the creation of multiple different uses of the bots 
while keeping the program running at all times. This feature allows 
me to focus the efforts of the bots, even as the program runs 24/7. 
On a whim I can change the focus of the bots from reconnaissance to 
targeting one of my videos. 

In theory I should be able to create multiple thread pools. 
"""
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored  
import random as r 

from classes.worker import TheiaWorker

class ThreadPool: 
    def __init__(self, id, mw, task): 
        self.id = id
        self.mw = mw
        self.task = task

        self.threadpool = ThreadPoolExecutor(max_workers=mw) 
        self.workers = [] 

        for worker_num in range(mw): 
            w = TheiaWorker(self.threadpool, (worker_num + 1), None)
            self.workers.append(w) 

    def __str__(self): 
        # Total - 60 
        return((f"[Thread Pool {self.id}]: {self.task}").ljust(59, "-") + "|")

    def getId(self): 
        return(self.id)

    def getWorkers(self): 
        return(self.workers)

    def getMaxWorkers(self): 
        return(self.mw)

    def getThreadPool(self):
        return(self.threadpool) 

    def __del__(self):
        self.threadpool.shutdown(wait=False)


# Project Theia v0.4, 01/07/23 
#------------------------------| IMPORTS / CONFIGURATIONS
import json, time, sys, os, random
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored  
from selenium import webdriver 

from classes.worker import TheiaWorker
from classes.threadpool import ThreadPool

EXTRAS = json.load(open('extra.json'))


#------------------------------| VARIABLES
active_threadpools = []

UP = "\x1B[1A" #up 1 
CLR = "\x1B[0K" #clear 


#------------------------------| MENU FUNCTIONS 
# [0] CLOSE PROGRAM 
# Just closes the program. 
def close_program(): 
    print("\nExiting... \n")
    os._exit(0)


# [1] PROCESS MANAGER 
# Shows threads and shit 
def process_manager(): 
    if len(active_threadpools) > 0:
        total_workers = 0 
        for threadpool in active_threadpools: 
            for worker in threadpool.getWorkers(): 
                total_workers += 1 
        
        print("\n"*(len(active_threadpools) + total_workers + 2))
        while True: 
            try: 
                time.sleep(0.3)
                print(f"{UP}"*(len(active_threadpools)+total_workers+3))
                for threadpool in active_threadpools: 
                    print(threadpool)
                    for worker in threadpool.getWorkers(): 
                        print(worker)
                print('\nPress \"CTRl+C\" to exit')
            except KeyboardInterrupt: 
                menu(True, "")
    else: 
        menu(True, EXTRAS["error"]["no_thread_pool"]) 


# [2] REMOVE BOTS 
def delete_threadpool(): 
    if len(active_threadpools) > 0:
        print("\nD")
        for x in range(len(active_threadpools)):
            print(f"[{str(x)}] {active_threadpools[x].getId()}")
        time.sleep(5)
          
    else: 
        menu(True, EXTRAS["error"]["no_thread_pool"])


# [3] MAKE BOTS 
# Makes bots
def create_threadpool(): 
    user_worker_input = int(input("Number of workers (threads): "))
    
    print("\nCreating threadpool for bots...")
    threadpool_index = f"bot_maker_{len(active_threadpools)}" 
    active_threadpools.append(ThreadPool(threadpool_index, user_worker_input, "(YT) Account creation"))
 
    menu(True, (f"Created bot {threadpool_index}"))


#------------------------------| MAIN 
menu_options = {"0": ("Exit", close_program),
                "1": ("Process manager", process_manager),
                "2": ("DELETE ThreadPool", delete_threadpool),                
                "3": ("CREATE ThreadPool", create_threadpool)}
def menu(refresh, message):
    if refresh: 
        divider, banner = EXTRAS["divider"], EXTRAS['banner']
        os.system("clear")
        print(f"{divider}\n{banner}{divider}\n >",colored(message, 'red')) 
    mo = menu_options
    for key in mo: print(f"[{key}] {mo[key][0]}")
    
    try: 
        menu_options.get(input("Make your choice: "))[1]()
    except: 
        menu(True, EXTRAS["error"]["command_unknown"]) 

menu(True, "")
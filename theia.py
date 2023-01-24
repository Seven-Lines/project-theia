# Project Theia v0.4.5, 01/24/23
#------------------------------| IMPORTS / CONFIGURATIONS
import json, time, sys, os, random
from threading import Thread
from termcolor import colored  
from selenium import webdriver 

from classes.worker import TheiaWorker
from classes.workerpool import workerpool

extr = json.load(open('extra.json'))

#------------------------------| VARIABLES
active_workerpools = []

UP = "\x1B[1A" #up 1 
CLR = "\x1B[0K" #clear 

version = "v0.5.0; 1/24/23"

#------------------------------| MENU FUNCTIONS 
# [0] "EXIT"
# Closes program. 
def close_program(): 
    print("\nExiting... \n")
    os._exit(0)


# [1] "PROCESS MANAGER" 
# Shows threads and shit. 
def process_manager(): 
    if len(active_workerpools) > 0:
        total_workers = 0 
        for wp in active_workerpools: 
            for worker in wp.getWorkers(): 
                total_workers += 1 
        
        print("\n"*(len(active_workerpools) + total_workers + 2))
        process = True 
        while process: 
            try: 
                time.sleep(0.3)
                print(f"{UP}"*(len(active_workerpools)+total_workers+3))
                for workerpool in active_workerpools: 
                    print(workerpool)
                    for w in workerpool.getWorkers(): 
                        print(w)
                print('\nPress \"CTRl+C\" to exit')
            except KeyboardInterrupt: 
                process = False
                menu(True, "We done with that shit")

    else: 
        menu(True, extr["error"]["no_thread_pool"]) 


# [2] "DELETE WORKERPOOL" 
# Deletes workerpool.
def delete_workerpool(): 
    if len(active_workerpools) > 0:
        print("\n")

        options = {"0": ("GO BACK", menu)}
        for x in range(len(active_workerpools)):
            options[str(x+1)] = (active_workerpools[x], active_workerpools[x].__del__)

        for key in options: 
            print(f"[{key}] {options[key][0]}")
        try: 
            choice = options.get(str(input("Make your choice: ")))      
            active_workerpools.remove(choice[0])
            choice[1]()
            menu(True, extr["message"]["deleted_workerpool"].format(choice[0].getId()))
        except: 
            menu(True, extr["error"]["failed_to_delete"])        
    else: 
        menu(True, extr["error"]["no_thread_pool"])


# [3] "CREATE WORKERPOOL" 
# Creates pool of workers.
def create_workerpool(): 
    user_worker_input = int(input("Number of workers (threads): "))
    
    print("\nCreating workerpool for bots...")
    workerpool_index = f"bot_maker_{len(active_workerpools)}" 
    active_workerpools.append(workerpool(workerpool_index, user_worker_input, "(YT) Account creation"))
 
    menu(True, (f"Created bot {workerpool_index}"))


#------------------------------| MAIN 
def menu(refresh, message):
    menu_options = {"0": ("Exit", close_program),
                "1": ("Process manager", process_manager),
                "2": ("DELETE workerpool", delete_workerpool),                
                "3": ("CREATE workerpool", create_workerpool)}
    if refresh: 
        divider, banner = extr["divider"], extr['banner'].format(version)
        os.system("clear")
        print(f"{divider}\n{banner}{divider}\n >",colored(message, 'red')) 
    for key in menu_options: print(f"[{key}] {menu_options[key][0]}")
    
    try: 
        menu_options.get(input("Make your choice: "))[1]()
    except: 
        if message != None: 
            menu(True, message)
        else: 
            menu(True, extr["error"]["command_unknown"]) 

menu(True, "")
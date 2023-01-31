# Project Theia v0.4.5, 01/24/23
#------------------------------| IMPORTS / CONFIGURATIONS
import json, time, sys, os, random
from termcolor import colored  
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
        total_workers = sum(len(w.getWorkers()) for w in active_workerpools)
        print("\n"*(len(active_workerpools) + total_workers + 2))
        process = True 
        while process: 
            try: 
                time.sleep(0.3)
                print(f"{UP}"*(len(active_workerpools) + total_workers + 3))
                for wp in active_workerpools: print(wp); [print(w) for w in wp.getWorkers()]
                print('\nPress \"CTRl+C\" to exit')
            except KeyboardInterrupt: 
                process = False
                menu(True, "")

    else: 
        menu(True, extr["error"]["no_thread_pool"]) 

# [2] "CREATE WORKERPOOL" 
# Creates pool of workers.
def create_workerpool(): 
    options = {"0": ("Idk")}
    user_worker_input = int(input("Number of workers (threads): "))
    
    #def workerpool_processer(task):

    print("\nCreating workerpool for bots...")
    workerpool_index = f"bot_maker_{len(active_workerpools)}" 
    active_workerpools.append(workerpool(workerpool_index, user_worker_input, "NULL task"))
 
    menu(True, (f"Created bot {workerpool_index}"))


# [3] "DELETE WORKERPOOL" 
# Deletes workerpool.
def delete_workerpool(): 
    if len(active_workerpools) > 0:
        print("\n")

        options = {"0": "GO BACK"}
        [options.update({str(wp[0]+1): wp[1]}) for wp in enumerate(active_workerpools)]
        [print(f"[{key}] {options[key]}") for key in options]
        try: 
            choice = options.get(str(input("Make your choice: ")))      
            active_workerpools.remove(choice)
            choice.__del__()
            menu(True, extr["message"]["deleted_workerpool"].format(choice.getId()))
        except: 
            menu(True, extr["error"]["failed_to_delete"])        
    else: 
        menu(True, extr["error"]["no_thread_pool"])


#------------------------------| MAIN 
def menu(refresh, message):
    menu_options = {"0": ("Exit", close_program),
                "1": ("Process manager", process_manager),
                "2": ("CREATE workerpool", create_workerpool),                
                "3": ("DELETE workerpool", delete_workerpool)}
    if refresh: 
        divider, banner = extr["divider"], extr['banner'].format(version)
        os.system("clear")
        print(f"{divider}\n{banner}{divider}\n >",colored(message, 'red')) 
    [print(f"[{key}] {menu_options[key][0]}") for key in menu_options] 
    
    try: 
        menu_options.get(input("Make your choice: "))[1]()
    except: 
        if message != None: 
            menu(True, message)
        else: 
            menu(True, extr["error"]["command_unknown"]) 

menu(True, "")
""" -----| THEIA WORKER CLASS 
This is what defines the individual behavior of each 
of the workers that inhabit the threadpool.
"""
import random, time 
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

webdriver_executable = '~/Documents/GitHub/project-theia/WebDrivers/chromedriver.exe'

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
#------------------------------| TEST/THREADING  
def test_threading(worker):
    test_status = [ 
        "Getting selenium", 
        "Finding victim", 
        "Logging into account"
    ]

    while True: 
        worker.status = test_status[random.randint(0, 2)]
        time.sleep(random.randint(0, 2))
    

#------------------------------| TEST/SELENIUM
def test_selenium(worker): 
    worker.status = "Configuring selenium"

    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    #options.headless = True 
    #options.add_argument('--proxy-server=%s' %proxy)
    options.add_argument('--window-size=640,480')

    worker.status = "Opening web browser"

    try: 
        driver = webdriver.Chrome(service=Service(webdriver_executable), options=options)
        driver.get("https://www.google.com/webhp?hl=en&ictx=2&sa=X&ved=0ahUKEwjt7qadq4b9AhXCgoQIHWhVA5EQPQgK")
    except: 
        worker.status = "BROKEN" 
        time.sleep(3)


#------------------------------| MAKE BOTS
def make_bots(worker):
    worker.status = "Configuring selenium"

    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    #options.headless = True
    #options.add_argument('--proxy-server=%s' %proxy)
    options.add_argument('--window-size=640,480')

    worker.status = "Creating random variables"

    username = "username"
    password = "password"

    


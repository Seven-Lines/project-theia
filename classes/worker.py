""" -----| THEIA WORKER CLASS 
This is what defines the individual behavior of each 
of the workers that inhabit the threadpool.
"""
import random, time, json

from termcolor import colored  
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

webdriver_executable = '~/Documents/GitHub/project-theia/WebDrivers/chromedriver.exe'
extr = json.load(open('extra.json'))

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
success = "\033[92mSUCCESS\033[0m"
failure = "\033[91mFAILURE\033[0m"
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
    options.headless = True 
    #options.add_argument('--proxy-server=%s' %proxy)
    options.add_argument('--window-size=640,480')

    worker.status = "Opening web browser"

    try: 
        driver = webdriver.Chrome(service=Service(webdriver_executable), options=options)
        driver.get(extr["links"]["google"])
    except: 
        worker.status = failure 
        time.sleep(3)

    #worker.status = extr["message"]["success"]
    worker.status = success

#------------------------------| MAKE BOTS
def make_bots(worker):
    try: 
        worker.status = "Configuring selenium"

        options = ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        #options.headless = True
        #options.add_argument('--proxy-server=%s' %proxy)
        options.add_argument('--window-size=640,480')

        worker.status = "Opening GuerrillaMail"

        driver = webdriver.Chrome(service=Service(webdriver_executable), options=options)
        driver.get(extr["link"]["guerillamail"])

        worker.status = "Opening ProtonMail Sign Up"
        driver.execute_script("window.open('about:blank', 'secondtab');")

        time.sleep(5)
    except: 
        worker.status = failure


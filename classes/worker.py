""" -----| THEIA WORKER CLASS 
This is what defines the individual behavior of each 
of the workers that inhabit the threadpool.
"""
import random, time, json, string

from termcolor import colored  
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from guerrillamail import GuerrillaMailSession

webdriver_executable = '~/Documents/GitHub/project-theia/WebDrivers/chromedriver.exe'
extr = json.load(open('extra.json'))

class TheiaWorker: 
    def __init__(self, threadpool, id_num, status):
        self.threadpool = threadpool
        self.id_num = id_num 
        self.status = status 
    
    def __str__(self): 
        return((f"  ↳ Worker {self.id_num}") + (f"{self.status}").rjust(48, ".") + " ")
    

""" -----| THEIA WORKER BEHAVIOR 
These are the functions that the workers 
actually inact. Idk, I'm fat and retarded bro.
"""
success = "! SUCCESS !"
failure = "! FAILURE !"
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
    worker.status = "Configuring selenium"
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    #options.headless = True
    #options.add_argument('--proxy-server=%s' %proxy)
    options.add_argument('--window-size=640,480')

    driver = webdriver.Chrome(service=Service(webdriver_executable), options=options)

    try: 
        #---> NAME 
        worker.status = "Generating random name"
        first_names, last_names = json.load(open('./data/word_lists/first_names.json')), json.load(open('./data/word_lists/last_names.json')) 
        name = f"{first_names[random.randint(1, 999)]} {last_names[random.randint(1, 999)]}"
        
        #---> USERNAME
        worker.status = "Generating random username"
        match random.randint(1, 3): 
            case 1: 
                print("noun")
            case 2: 
                print("adjective+noun")
            case 3: 
                print("wiki")
                driver.get(extr["links"]["random_wiki"])

        user = "username"

        #---> PASSWORD 
        worker.status = "Generating random password"
        pas = "password"

        #---> EMAIL
        worker.status = "Generating random email"

        driver.get()
        temp = driver.find_element(By.CLASS_NAME, "firstHeading").text
        print(temp)

        print(name)
        time.sleep(5)

        driver.get(extr["links"]["protonmail"]["signup"])

        guerrilla_mail_session = GuerrillaMailSession()
        temp_email = guerrilla_mail_session.get_session_state()['email_address']

        email = "email"

    except: 
        worker.status = failure
 
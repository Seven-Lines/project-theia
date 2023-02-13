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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from guerrillamail import GuerrillaMailSession

from util.username_generator import ru_name, ru_noun
from util.password_generator import rp_rand

webdriver_executable = '~/Documents/GitHub/project-theia/chromedriver.exe'
extr = json.load(open('./data/extra.json'))

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
    options.add_argument('--window-size=800,1000')

    driver = webdriver.Chrome(service=Service(webdriver_executable), options=options)

    try: 
        worker.status = "Generating random credentials"
        #---> NAME
        first_names, last_names = json.load(open('./data/word_lists/first_names.json')), json.load(open('./data/word_lists/last_names.json')) 
        name = f"{first_names[random.randint(1, 999)]} {last_names[random.randint(1, 999)]}"
        
        #---> USERNAME
        match random.randint(1, 2): 
            case 1: usr = ru_name(name) 
            case 2: usr = ru_noun(name)

        #---> PASSWORD 
        pas = rp_rand()

        #---> EMAIL (& RECOVERY EMAIL)
        worker.status = "Creating GuerrillaMail session"
        email_handle = ru_name(name)
        gm_session = GuerrillaMailSession()
        gm_session.set_email_address(email_handle)
        
        worker.status = "Waiting for ProtonMail to respond"
        driver.get(extr["links"]["protonmail"]["signup"])
        
        worker.status = "Inputing credentials to ProtonMail"
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH, extr["xpaths"]["proton"]["password"]))).send_keys(pas)
        wait.until(EC.element_to_be_clickable((By.XPATH, extr["xpaths"]["proton"]["repeat_password"]))).send_keys(pas)
        driver.switch_to.frame(driver.find_element(By.XPATH, extr["xpaths"]["proton"]["username_iframe"]))
        driver.find_element(By.XPATH, extr["xpaths"]["proton"]["username"]).send_keys(usr)
        driver.switch_to.default_content()
        driver.find_element(By.XPATH, extr["xpaths"]["proton"]["create_account_button"]).click()
        
        worker.status = "Sending verification to fake email"
        wait.until(EC.element_to_be_clickable((By.XPATH, extr["xpaths"]["proton"]["email_tab"]))).click()
        
        def get_random_domain(): 
            return(random.choice(["sharklasers.com", "guerrillamail.info", "grr.la", "guerrillamail.biz", "guerrillamail.com", 
                                "guerrillamail.de", "guerrillamail.net", "guerrillamail.org", "guerrillamailblock.com", 
                                "pokemail.net", "spam4.me"]))
                
        wait.until(EC.element_to_be_clickable((By.XPATH, extr["xpaths"]["proton"]["email"]))).send_keys(f"{email_handle}@{get_random_domain()}")
        # error check at this point, if domain doesn't work call domain function again.  
        driver.find_element(By.XPATH, extr["xpaths"]["proton"]["verification_code_button"]).click()

        worker.status = "Waiting to receieve verification code"
        verification_code = "000000"
        while True:
            latest_email = gm_session.get_email_list()[0]
            if(latest_email.subject == "Proton Verification Code"): 
                verification_code = latest_email.excerpt.split()[5]
                break
            else: 
                time.sleep(3)

        worker.status = f"Using verification code {verification_code}"
        wait.until(EC.element_to_be_clickable((By.XPATH, extr["xpaths"]["proton"]["verification_code"]))).send_keys(verification_code)
        wait.until(EC.element_to_be_clickable((By.XPATH, extr["xpaths"]["proton"]["verification_button"]))).click()        

        worker.status = "Finishing creating account"
        #wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div/div/main/div[2]/form/button'))).click()        
        #wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div/div/main/div[2]/form/button[1]'))).click() 

        while True: 
            time.sleep(2)

        #email = f"{email_handle}@protonmail.com" #.. not complete btw 
    except: 
        worker.status = failure

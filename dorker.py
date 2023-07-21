import os
import random
import sys
import threading
import time
import urllib
from urllib.parse import urlparse
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

##################################### BY @Unix_xD #######################################################

browsers = ['Chrome', 'Firefox']

optn = [{'os': 'Windows',
         'osVersion': '11',
         'debug': 'true',
         "networkLogs": "true",
         'consoleLogs': 'info',
         'browserVersion': 'latest'},
        {'os': 'Windows',
         'osVersion': '10',
         'debug': 'true',
         "networkLogs": "true",
         'consoleLogs': 'info',
         'browserVersion': 'latest'},
        {'os': 'OS X',
         'osVersion': 'Big Sur',
         'debug': 'true',
         "networkLogs": "true",
         'consoleLogs': 'info',
         'browserVersion': 'latest'},
        {'os': 'OS X',
         'osVersion': 'Monterey',
         'debug': 'true',
         "networkLogs": "true",
         'consoleLogs': 'info',
         'browserVersion': 'latest'},
        {'os': 'OS X',
         'osVersion': 'Ventura',
         'debug': 'true',
         "networkLogs": "true",
         'consoleLogs': 'info',
         'browserVersion': 'latest'},
        {'os': 'OS X',
         'osVersion': 'Catalina',
         'debug': 'true',
         "networkLogs": "true",
         'consoleLogs': 'info',
         'browserVersion': 'latest'},
        {'os': 'OS X',
         'osVersion': 'Mojave',
         'debug': 'true',
         "networkLogs": "true",
         'consoleLogs': 'info',
         'browserVersion': 'latest'}]


class Dorker:
    def parseUrl(self, site):
        return urlparse(site).netloc


    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def log(self, msg):
        timer = datetime.now().strftime("%H:%M:%S")
        print(f'{Fore.GREEN}[+] [{timer}] Dorker:{Style.RESET_ALL} {msg}')


    def loga(self, msg):
        timer = datetime.now().strftime("%H:%M:%S")
        print(f'{Fore.BLUE}[+] [{timer}] Dorker:{Style.RESET_ALL} {msg}')


    def logb(self, msg):
        timer = datetime.now().strftime("%H:%M:%S")
        print(f'{Fore.RED}[!] [{timer}] Dorker:{Style.RESET_ALL} {msg}')
        

    def banner(self):
        self.clear()
        logo = (""" 
    ██████╗  ██████╗  ██████╗  ██████╗ ██╗     ███████╗    ██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗██████╗     ██████╗ ██████╗  ██████╗ 
    ██╔════╝ ██╔═══██╗██╔═══██╗██╔════╝ ██║     ██╔════╝    ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗
    ██║  ███╗██║   ██║██║   ██║██║  ███╗██║     █████╗      ██║  ██║██║   ██║██████╔╝█████╔╝ █████╗  ██████╔╝    ██████╔╝██████╔╝██║   ██║
    ██║   ██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝      ██║  ██║██║   ██║██╔══██╗██╔═██╗ ██╔══╝  ██╔══██╗    ██╔═══╝ ██╔══██╗██║   ██║
    ╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗    ██████╔╝╚██████╔╝██║  ██║██║  ██╗███████╗██║  ██║    ██║     ██║  ██║╚██████╔╝
    ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ 
                                                                                                                                        
    """)
        for col in logo:
            print(Fore.GREEN + col, end="")
            sys.stdout.flush()
            time.sleep(0.0025)
        print(Style.RESET_ALL)
        print('made by: @Unix_xD')
    

    def google_search(self, qry, acc):
        amb = []
        result = self.worker(qry, acc)
        for il in result:
            if il not in amb:
                amb.append(il)
        self.loga(f'Total URLs from {qry} = {str(len(amb))}')
        open('results.txt', 'a', encoding='utf-8').write('\n'.join(amb) + '\n')


    def worker(self, query, acc, start=0, rslt=None, domain=None):
        acc = acc.strip()
        if rslt is None:
            rslt = []
        if domain is None:
            domain = []
        options = Options()
        BROWSERSTACK_USERNAME = acc.split(':')[0]
        BROWSERSTACK_ACCESS_KEY = acc.split(':')[1]
        URL = "https://{}:{}@hub.browserstack.com/wd/hub".format(BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY)
        bstack_options = random.choice(optn)
        options.set_capability('bstack:options', bstack_options)
        options.set_capability('browserName', random.choice(browsers))
        driver = webdriver.Remote(command_executor=URL, options=options)
        self.loga("Started!")
        time.sleep(3)
        oq = query
        query = urllib.parse.quote_plus(query)
        while True:
            url = f"https://google.com/search?q={query}&start={start}&num=100&filter=1"
            driver.get(url)
            time.sleep(2)
            if 'https://www.google.com/sorry/index' in driver.current_url:
                driver.quit()
                self.logb('RECAPTCHA!')
                time.sleep(5)
                return self.worker(oq, acc, start, rslt, domain)
            try:
                xs = driver.find_element(By.XPATH, "/html//div[@id='topstuff']//p[@role='heading']").text
                if 'did not match any documents.' in xs:
                    driver.quit()
                    self.loga(f"Finished {oq}!")
                    time.sleep(5) # Time gap between stopping and starting a new instance
                    return rslt
            except:
                pass
            try:
                WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="yuRUbf"]/a')))
            except:
                driver.quit()
                self.loga(f"Finished {oq}!")
                time.sleep(5) # Time gap between stopping and starting a new instance
                return rslt
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, "html.parser")
            search_results = soup.select('div.yuRUbf > a')
            result_links = [result['href'] for result in search_results]
            self.loga(f'Total URLs in this Page = {str(len(result_links))}')
            for ix in result_links:
                if self.parseUrl(ix) not in domain:
                    domain.append(self.parseUrl(ix))
                    rslt.append(ix)
                    self.log(self.parseUrl(ix))

            self.loga('NEXT PAGE!')
            start += 100


def start_threads(lst):
    with open('accounts.txt', encoding='utf-8') as f:
        accounts = [line.strip() for line in f]
    xdc = len(accounts)

    parameters = [line.strip() for line in lst]

    account_locks = {account: threading.Lock() for account in accounts}
    threads = []
    for i in range(0, len(parameters)):
        dorkr = Dorker()
        
        thread = threading.Thread(target=dorkr.google_search, args=(parameters[i], accounts[i % len(accounts)]))
        threads.append(thread)
        while threading.active_count() >= xdc + 1:
            pass
        thread.start()

    for thread in threads:
        thread.join()
    dorkr.clear()


bsc = Dorker()
bsc.banner()
fp = input(f"{Fore.RED}[!] Enter your file name containing Dorks: {Style.RESET_ALL}")

encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'utf-16', 'utf-32', 'windows-1252', 'ascii', 'cp437']

for encoding in encodings:
    try:
        dorks = open(fp, 'r', encoding=encoding).readlines()
        break
    except UnicodeDecodeError:
        bsc.logb(f"Decoding failed with encoding: {encoding}")
    except FileNotFoundError:
        bsc.logb("File not found!")
        sys.exit()

if dorks is None:
    bsc.logb('File invalid')
    sys.exit()

open('results.txt', 'w', encoding='utf-8').write('')
start_threads(dorks)
bsc.logb("Total URLs found = "+str(len(open('results.txt', 'r').readlines())))
bsc.loga("Now removing duplicate domains")


def remove_duplicate_domains(urls):
    unique_domains = set()
    result = []
    for url in urls:
        domain = bsc.parseUrl(url)
        if domain not in unique_domains:
            unique_domains.add(domain)
            result.append(url)
    return result


filename = "results.txt"
with open(filename, "r") as file:
    urls = file.read().splitlines()

unique_urls = remove_duplicate_domains(urls)
bsc.logb(f'Total Unique domains from {str(len(unique_urls))} URLs = {str(len(urls))}')
open('results.txt', 'w', encoding='utf-8').write('\n'.join(unique_urls))

"""Autologin Ldap quickly"""

# all imported libraries

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import argparse

# parsing the file passed as argument

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()
with args.file as file:
    content = file.readlines()
content = [x.strip() for x in content]

#username and password

username = content[0] # Your LDAP username
password = content[1] # Your LDAP passsword,

# setting up the webdriver using PhantomJS

driver = webdriver.PhantomJS()
driver.get("https://internet.iitb.ac.in/index.php")
delay = 3

# wait for the page to load

try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/table[1]/tbody/tr/td/table/tbody/tr/td[2]/font/h1')))
    print "Page is ready!"
except TimeoutException:
    print "Loading took too much time!"
    driver.close()

# attempt logging in
try:
    ip = driver.find_element_by_xpath("/html/body/center/center[2]/div/table/tbody/tr/td[2]/center")
    print("Already Logged in")
except:
    print("Attempting logging")
    u = driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[3]/form/table/tbody/tr[2]/td[1]/input")
    p = driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[3]/form/table/tbody/tr[2]/td[2]/input")
    u.send_keys(username)
    p.send_keys(password)
    driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[3]/form/table/tbody/tr[2]/td[3]/input").click()
    if driver.find_elements_by_xpath("//*[contains(., 'Login Failed!')]"):
        print "Bad Username or Password"
    else:
        print "Login Sucessful"

driver.close()

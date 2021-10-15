from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

#reading id and password from file
id_pass_file = open ("/home/kali/gid_pass.txt", "r")
id_pass = (id_pass_file.readlines())

gmail_id = id_pass[0]
gpass = id_pass[1]

#opening scoopit website
driver = webdriver.Firefox()
driver.get('https://www.scoop.it/login')
time.sleep(3)

#Logging in with the credentials
driver.find_element_by_name("email").send_keys(gmail_id)
driver.find_element_by_name("password").send_keys(gpass)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div[4]/div/button").click()

#for closing the suggestions dialogue box if it pops-up 
try:
    driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[3]/div/div/div/div[1]/div[2]").click()
except:
    print("Dialogue Box Not Found")

time.sleep(2)


count = 4

while count < 18:
    urlFile = open("/home/kali/anchorlinks.txt", "r")
    anchorUrls = (urlFile.readlines())

    titleFile = open("/home/kali/anchortitles.txt", "r")
    anchorTiltes = (titleFile.readlines())

    #inputing the URL in the url box
    driver.find_element_by_id("urlChooserField").send_keys(anchorUrls[count])
    time.sleep(3)
    driver.find_element_by_id("urlChooserButton").click()
    time.sleep(6)

    driver.find_element_by_xpath("/html/body/div[8]/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/span/input").send_keys(anchorTiltes[count])
    driver.find_element_by_xpath("/html/body/div[8]/div/div/div/div[2]/div/div/div[2]/div[2]/div/div").click()

    count += 1

    time.sleep(5)
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip as pc
import time
from getpass import getpass

def selectAll():
    act=ActionChains(driver)
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

def copy():
    act=ActionChains(driver)
    act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

def paste():
    act=ActionChains(driver)
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()



username = "cobiw51748"
password = "Acobiw51748@smuvaj.com1"


driver = webdriver.Firefox()
driver.get("https://www.folkd.com/")
#time.sleep(3)

#Clicking on Login Button
loginButton = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/a[4]")
loginButton.click()

#Providing Inputs to Login Page
usernameBox = driver.find_element_by_css_selector("#username")
usernameBox.send_keys(username)

passwordBox = driver.find_element_by_css_selector("#password")
passwordBox.send_keys(password)

submitButton = driver.find_element_by_css_selector("#submit_login")
submitButton.click()

count = 0

while count < 18 :

    #Clicking on add link button
    addLink = driver.find_element_by_css_selector("#subheader > a:nth-child(6)")
    addLink.click()

    saveasVideo = driver.find_element_by_xpath("/html/body/div[2]/div[4]/form[1]/ul/li[3]/input")
    saveasVideo.click()

    urlFile = open("/home/kali/anchorlinks.txt", "r")
    anchorUrls = (urlFile.readlines())

    titleFile = open("/home/kali/anchortitles.txt", "r")
    anchorTiltes = (titleFile.readlines())

    #inputing url in url box
    urlBox = driver.find_element_by_css_selector("#url_page")
    urlBox.click()
    selectAll
    urlBox.send_keys(anchorUrls[count])

    submitButton = driver.find_element_by_xpath("/html/body/div[2]/div[4]/form[1]/button").click()

    titleBox = driver.find_element_by_id("add_title").send_keys(anchorTiltes[count])
    tagsBox = driver.find_element_by_id("add_tags_show").send_keys(anchorTiltes[count])

    lastSubmitButton = driver.find_element_by_xpath("/html/body/div[2]/div[4]/form/p/input").click()

    folkdLink = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div[2]/h3/a").get_attribute('href')

    folkdFile = open("/home/kali/folkdUrls.txt", "a")
    folkdFile.write(folkdLink + "\n" )
    count += 1














# driver.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fu%2F0%2F&followup=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fu%2F0%2F&ltmpl=sheets&flowName=GlifWebSignIn&flowEntry=ServiceLogin', 'new window')")
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(3)

# gmailBox = driver.find_element_by_xpath('//*[@id ="identifierId"]').send_keys(gmail)
# nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
# nextButton[0].click()
# time.sleep(3)

# gpassBox = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
# gpassBox.send_keys(gpass)
# nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
# nextButton[0].click()

# time.sleep(3)


from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip as pc
import time
from tkinter import filedialog
import os


#pyperclip functions for copy pasting if we want to
def selectAll():
    act=ActionChains(driver)
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

def copy():
    act=ActionChains(driver)
    act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

def paste():
    act=ActionChains(driver)
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()





#assigning vairables a value as check if they are appended it means the fields are given proper values
login_access = 0
tags_value = 0
title_value = 0
file_value = 0
proceeding_to_sel = 0





#Giving a readme file to give basic instructions
def readmefunc():

    window = Tk()
    window.geometry("1100x500")
    window.minsize(1100,500)
    window.title("Things to Keep in mind")
    label1 = Label( window, text = "1. Do not use spaces or any special characters in the file names \n " +
    "2. Do not use tags longer than 1 line, if it goes in another line the tag will be assigned to the next link\n" +
    "3. Make sure the URLs, Titles and Tags are in the same order in all 3 files to avoid mix-match of the content\n" +
    "4. If you don't want to choose the Location of files then paste all three files in the same directory of the program.\n" +
    "and rename them as urls.txt, titles.txt, tags.txt(No capitalisation No nothing)" , font =25 , fg = "#5ba1cd", bg ="#212634")
    label1.pack()
    
    
    window.mainloop()


#func to go back on main screen
def back():
    second_win.destroy()
    main_screen()

def third_back():
    third_win.destroy()
    second_screen()

#func if the files are in the same Directory
def same_dir_files():
    global urlFilePath
    global titleFilePath
    global tagsFilePath
    global file_value
    global title_value
    global tags_value

    current_dir_back = os.getcwd()
    current_dir = current_dir_back.replace('\\', '/')
    urlFilePath = current_dir+"/urls.txt"
    titleFilePath = current_dir+"/titles.txt"
    tagsFilePath =  current_dir+"/tags.txt"

    file_value = 1
    title_value = 2
    tags_value = 3


    third_screen()
    second_win.destroy()





#Function to extract File path from the tkinter button 
def filePath():
    global urlFilePath
    urlFilePath = filedialog.askopenfilename(initialdir = "/", title = "Select a File for URLs", filetypes = (("Text files","*.txt*"),("All Files","*")))
    if urlFilePath:
        urlPathLabel = Label(second_win, text= urlFilePath, fg = "#90d58a", bg = "#212634")
        urlPathLabel.place(x=250, y=100)
        global file_value
        file_value = 1




#function to extract title file path 
def titlePath():
    global titleFilePath
    titleFilePath = filedialog.askopenfilename(initialdir = "/", title = "Select a File for Titles", filetypes = (("Text files","*txt*"), ("All Files", "*")))
    if titleFilePath:
        titlePathLabel = Label(second_win, text = titleFilePath, fg = "#90d58a", bg = "#212634")
        titlePathLabel.place(x=250, y=150)
        global title_value
        title_value = 2




#function to extract tags file path
def tagsPath():
    global tagsFilePath
    tagsFilePath = filedialog.askopenfilename(initialdir = "/", title = "Select a File for Tags", filetypes= (("Text files","*txt*"), ("All Files", "*")))
    if tagsFilePath:
        tagspathLabel = Label(second_win, text = tagsFilePath, fg = "#90d58a", bg = "#212634")
        tagspathLabel.place(x=250, y=200) 
        global tags_value
        tags_value = 3



#function to capture the folkd credentials and also check if all the fields are provided with the input
def proceed():
    global login_access
    global folkd_user
    global folkd_pass
    global scoopit_user
    global scoopit_pass
    global proceeding_to_sel
    user_field = user_entry.get()
    pass_field = pass_entry.get()


    #assigning a value to close the window
    if win_value == 2:
        win_name = second_win
    elif win_value == 3:
        win_name = third_win

    if (user_field == "" or pass_field == ""):
        messagebox.showinfo("", "Please Enter the Credentials")
    else:
        login_access = 4

        if login_access + title_value + file_value + tags_value == 10:
            messagebox.showinfo("", "Proceeding......")
            win_name.destroy()
        else:
            messagebox.showinfo("", "Something is missing please check and try again")

    
    if con == "folkd":
        folkd_user = user_field
        folkd_pass = pass_field
        proceeding_to_sel = 1
    elif con == "scoopit":
        scoopit_user = user_field
        scoopit_pass = pass_field
        proceeding_to_sel = 2





#Giving Variables for requested Automation
def func_rqst(rqst):
    global title
    global user_var
    global pass_var
    global proceed_func
    global con
    con = rqst
    if con == "folkd":
        title = "Folkd Bookmarking"
        user_var = "Folkd Username"
        pass_var = "Folkd Password"

    elif con == "scoopit":
        title = "Scoopit Bookmarking"
        user_var = "Scoopit Username"
        pass_var = "Scoopit Password"

    window.destroy()
    second_screen()




def third_screen():
    global user_entry
    global pass_entry
    global third_win
    global win_value

    win_value = 3
    
    third_win = Tk()
    third_win.title(title)
    third_win.geometry("700x500")
    third_win.minsize(500, 400)
    third_win.configure(bg = "#212634")

    user_label = Label(third_win, text = user_var, fg = "#90d58a", bg = "#212634")
    user_label.place(x=20, y=20)
    user_entry = Entry(third_win)
    user_entry.place(x = 150, y = 20)
    user_entry.configure(fg = "#3a85d7", bg = "#14344b")

    pass_label = Label(third_win , text= pass_var, fg = "#90d58a", bg = "#212634")
    pass_label.place(x=20, y=60)
    pass_entry = Entry(third_win)
    pass_entry.place(x=150, y=60)
    pass_entry.config(show="*")
    pass_entry.configure(fg = "#3a85d7", bg = "#14344b")


    urlPathLabel = Label(third_win, text= "Path for URL file " + urlFilePath, fg = "#90d58a", bg = "#212634")
    urlPathLabel.place(x=40, y= 100)

    titlePathLabel = Label(third_win, text = "Path for Title file " + titleFilePath, fg = "#90d58a", bg = "#212634")
    titlePathLabel.place(x=40, y= 150)
    
    tagsPathLabel = Label(third_win, text = "Path for Tags file " + tagsFilePath, fg = "#90d58a", bg = "#212634")
    tagsPathLabel.place(x=40, y= 200)

    back_button = Button(third_win, text= "Back", command = third_back, width = 8, height = 1, bg = "#2e333e" , fg = "#90d58a")
    back_button.place(x = 450, y = 20)

    readme = Button(third_win, text= "Readme", command = readmefunc, width = 8, height = 1, bg = "#2e333e" , fg = "#90d58a")
    readme.place(x=40, y = 250)

    proceed_button = Button(third_win, text = "Proceed", command = proceed, width = 8, height = 1, bg = "#2e333e" , fg = "#90d58a")
    proceed_button.place(x= 305, y = 350)


def second_screen():
    global user_entry
    global pass_entry
    global second_win
    global win_value

    win_value = 2

    second_win = Tk()
    second_win.title(title)
    second_win.geometry("700x500")
    second_win.minsize(500, 400)
    second_win.configure(bg = "#212634")

    user_label = Label(second_win, text = user_var, fg = "#90d58a", bg = "#212634")
    user_label.place(x=20, y=20)
    user_entry = Entry(second_win)
    user_entry.place(x = 150, y = 20)
    user_entry.configure(fg = "#3a85d7", bg = "#14344b")

    pass_label = Label(second_win , text= pass_var, fg = "#90d58a", bg = "#212634")
    pass_label.place(x=20, y=60)
    pass_entry = Entry(second_win)
    pass_entry.place(x=150, y=60)
    pass_entry.config(show="*")
    pass_entry.configure(fg = "#3a85d7", bg = "#14344b")

    url_path = Button(second_win, text= "File for Content's URLs", command = filePath, width = 20, height = 1, bg = "#2e333e" , fg = "#90d58a")
    url_path.place(x=40, y= 100)
    
    title_path = Button(second_win, text= "File for Content's Titles", command = titlePath,  width = 20, height = 1, bg = "#2e333e" , fg = "#90d58a")
    title_path.place(x=40, y= 150)
    
    
    tags_path = Button(second_win, text= "File for Content's Tags", command = tagsPath, width = 20, height = 1, bg = "#2e333e" , fg = "#90d58a")
    tags_path.place(x=40, y= 200)

    readme = Button(second_win, text= "Readme", command = readmefunc, width = 8, height = 1, bg = "#2e333e" , fg = "#90d58a")
    readme.place(x=40, y = 250)

    proceed_button = Button(second_win, text = "Proceed", command = proceed, width = 8, height = 1, bg = "#2e333e" , fg = "#90d58a")
    proceed_button.place(x= 305, y = 350)

    back_button = Button(second_win, text= "Back", command = back, width = 8, height = 1, bg = "#2e333e" , fg = "#90d58a")
    back_button.place(x = 450, y = 20)
      
    same_dir_button = Button(second_win, text= "If Files are in the same Folder", command = same_dir_files, width = 25, height = 1, bg = "#2e333e" , fg = "#90d58a")
    same_dir_button.place(x = 450, y = 80)
    second_win.mainloop()





def main_screen():
    global window
    window = Tk()
    window.geometry("700x650")
    window.minsize(700,600)
    window.title("Social Bookmarking Automation")
    window.configure(bg = "#212634")

    folkd_button = Button(text = "Folkd Automation", command = lambda *args:func_rqst("folkd")  , width = 16, height = 1, bg = "#2e333e" , fg = "#90d58a")
    folkd_button.place(x = 40, y = 40)
    
    scoopit_button = Button(text= "Scoopit Automation", command = lambda *args:func_rqst("scoopit"), width = 16, height = 1, bg = "#2e333e" , fg = "#90d58a")
    scoopit_button.place(x = 40, y = 80)

    readme = Button(text= "Readme", command = readmefunc, width = 8, height = 1, bg = "#2e333e" , fg = "#90d58a")
    readme.place(x=20, y = 600)


    window.mainloop()


main_screen()


#script for executing folkd script
def folkd_script():
    #assigning the vairables with username and password of folkd
    username = str(folkd_user)
    password = str(folkd_pass)

    global driver


    driver = webdriver.Firefox()
    driver.get("https://www.folkd.com/")
    time.sleep(3)


    #Clicking on Login Button
    loginButton = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/a[4]")
    loginButton.click()



    #Providing Inputs to Login Page
    usernameBox = driver.find_element_by_css_selector("#username")
    usernameBox.send_keys(username)

    passwordBox = driver.find_element_by_css_selector("#password")
    passwordBox.send_keys(password)

    #Clicking on Login Button
    submitButton = driver.find_element_by_css_selector("#submit_login")
    submitButton.click()

    count = 0
    #To check the number of URls in order to provide the while loop with a limit
    file = open(urlFilePath, "r")
    f = (urlFile.readlines())
    limit = len(f)

    #while loop will run for the n(number of URLs) times 
    while count < limit :

        #Clicking on add link button
        addLink = driver.find_element_by_css_selector("#subheader > a:nth-child(6)")
        addLink.click()

        #Giving it the format of the Link which is Mostly link
        saveasVideo = driver.find_element_by_xpath("/html/body/div[2]/div[4]/form[1]/ul/li[3]/input")
        saveasVideo.click()

        #opening the files of URLs,Titles and Tags
        urlFile = open(urlFilePath, "r")
        urls = (urlFile.readlines())

        titleFile = open(titleFilePath, "r")
        titles = (titleFile.readlines())

        tagsFile = open(tagsFilePath, "r")
        tags = (tagsFile.readlines())


        #inputing url in url box
        urlBox = driver.find_element_by_css_selector("#url_page")
        urlBox.click()
        selectAll()
        urlBox.send_keys(urls[count])

        submitButton = driver.find_element_by_xpath("/html/body/div[2]/div[4]/form[1]/button").click()
        
        #inputing the title and tags in titlebox and tagsbox respectively
        titleBox = driver.find_element_by_id("add_title").send_keys(titles[count])
        tagsBox = driver.find_element_by_id("add_tags_show").send_keys(tags[count])

        lastSubmitButton = driver.find_element_by_xpath("/html/body/div[2]/div[4]/form/p/input").click()

        #Fetchiing the Folkd Link
        folkdLink = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div[2]/h3/a").get_attribute('href')

        #Getting the directory and writing the links on a file
        folkd_link_save = os.getcwd()
        folkdFile = open(folkd_link_save, "a")
        folkdFile.write(folkdLink + "\n" )
        count += 1

#script for executing scoopit script
def scoopit_script():

    global driver 
    
    driver = webdriver.Firefox()
    driver.get("https://www.scoop.it/login")
    time.sleep(3)
    

    #Logging in with the credentials
    driver.find_element_by_name("email").send_keys(scoopit_user)
    driver.find_element_by_name("password").send_keys(scoopit_pass)
    time.sleep(3)
    driver.find_element_by_css_selector(".button").click()

    time.sleep(3)

    try:
        driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[3]/div/div/div/div[1]/div[2]").click()
    except:
        print("Dialogue Box Not Found")

    time.sleep(2)

    count = 0
    #To check the number of URls in order to provide the while loop with a limit
    file = open(urlFilePath, "r")
    f = file.readlines()
    limit = len(f)

    while count < limit:

        #opening the files of URLs,Titles and Tags
        urlFile = open(urlFilePath, "r")
        urls = (urlFile.readlines())

        titleFile = open(titleFilePath, "r")
        titles = (titleFile.readlines())

        tagsFile = open(tagsFilePath, "r")
        tags = (tagsFile.readlines())
        
        driver.find_element_by_id("urlChooserField").send_keys(urls[count])
        driver.find_element_by_id("urlChooserButton").click()

        time.sleep(4)

        driver.find_element_by_css_selector(".tagsEditorInput").send_keys(tags[count])

        title_box = driver.find_element_by_css_selector(".h-scoopitwindow-post-title")
        title_box.click()
        selectAll()
        title_box.send_keys(titles[count])
        

        driver.find_element_by_css_selector(".h-scoopitwindow-footer-right > div:nth-child(1) > div:nth-child(1)").click()

        time.sleep(3)

        count += 1


#Conditional statement to check if program have all values to proceed or not
if proceeding_to_sel == 1:
    folkd_script()
elif proceeding_to_sel == 2:
    scoopit_script()


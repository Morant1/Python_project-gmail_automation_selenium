from selenium import webdriver
import time


def email_check(username): # Before running, let's make sure the input is well-written
    user_length = len(username)
    structure = "@gmail.com"
    if user_length > len(structure):
         structure = "@gmail.com"
         email_part = username[-10:]
         counter = len(structure)-1
         for i in range(len(email_part)-1,0,-1):
                if email_part[i] != structure[counter]:
                  raise InputError(username)
                else:
                   counter-=1
         print("Email check succeed!")
    else:
        raise InputError(username)


class InputError(Exception):
    def __init__(self,arg):
        self._arg = arg
    def __str__(self):
        return 'Check you email:"{}" and try again' .format(self._arg)


def login(passwordStr,usernameStr):
    browser = webdriver.Chrome() # There's no need to insert PATH if you saved Chromedriver.exe in C:\Python\Scripts
    browser.get("http://www.gmail.com")
    username = browser.find_element_by_id('identifierId')  #log in with email
    username.send_keys(usernameStr)
    nextButton = browser.find_element_by_id('identifierNext') #press next
    nextButton.click()

    time.sleep(15)  # Waiting in order to let Selenium find elements
    password = browser.find_element_by_name('password') #insert password
    password.send_keys(passwordStr)

    signInButton = browser.find_element_by_id('passwordNext') #press next
    signInButton.click()



def main():
    username_ = input("Please insert your Email address:")
    username = username_
    email_check(str(username))
    pass_ = input("Please insert your password:")
    print("logging in...")
    login(pass_,username)

main()

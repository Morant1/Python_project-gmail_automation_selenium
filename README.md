## Gmail automation with selenium


### Prior requirements:

- [ ] Install selenium
- [ ] Install Google Chrome browser
- [ ] Download Selenium Chrome Driver according to your Chrome version [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [ ] Download the ZIP file, extract Chromedriver.exe executable and place it in your C:\Python\Scripts

###### *Selenium will allow us to scroll/copy text/fill forms and click buttons and Selenium Chrome Driver will open for us Google Chrome to perform our automated tasks .*

### Explaining the code:
##### Log in by using HTML attributes 

```
    username = browser.find_element_by_id('identifierId')  #log in with email
    username.send_keys(usernameStr) #simulates keypresses in the desired element
    nextButton = browser.find_element_by_id('identifierNext') #press next
    nextButton.click() #simulates a mouse click.
```

We need to find the input fields on the web page so we can enter our email and password.

- [ ] Use the built-in Chrome Developer Tools
- [ ] Right-click on the input fields, and select the “Inspect” menu
- [ ] Click on this sign: ![alt_text](images/click_html_.png) and place your mouse where the user inserts his email 

- [ ] finally, right-click the relevent field->copy->copy Xpath
###### *it will look like this:(Hebrew version)*
![alt_text](images/copy_Xpath_html.png)

- [ ] you will recieve this kind of text - "//*[@id="identifierId"]"
###### *In the code above, we are searching for the username input field by id, and filling it with the desired text 'identifierId'.*



- [x] I did the same exact process for 'Password' and 'Next' buttons.

#### Hope you'll find my explanation clear.
#### Now let's run the code ✔




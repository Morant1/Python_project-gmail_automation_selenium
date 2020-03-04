# Python_project-Facebook_automation

### Prior requirements:
- [ ] Install selenium
- [ ] Install Google Chrome browser
- [ ] Download Selenium Chrome Driver according to your Chrome version [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [ ] Download ZIP file, extract the chromedriver.exe executable, and place the your C:\Python\Scripts

###### *Selenium will allow us to scroll/copy text/fill forms and click buttons and Selenium Chrome Driver will open for us Google Chrome to perform our automated tasks .*

### Explaining the code:
###### Logging in with our email by using HTML attributes 

```
    username = browser.find_element_by_id('identifierId')  #log in with email
    username.send_keys(usernameStr)
    nextButton = browser.find_element_by_id('identifierNext') #press next
    nextButton.click()
```

We need to find the input fields on the web page so we can enter our email and password.

- [ ] Use the built-in Chrome Developer Tools
- [ ] ![We only need to right-click on the input fields, and select the “Inspect” menu](
![Test Image 1](copy_Xpath_html.png)




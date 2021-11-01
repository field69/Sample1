#importing the webdrivers from the selenium library
from Selenium import webdriver  

#importing another lib time
import time  
from Selenium.webdriver.common.keys import Keys

#notify that the script started
print("sample test case started")

#here in the Chrome() parentheses mention the complete path to the webriver of the browser which you have downloaded
driver = webdriver.Chrome()  

#optinal code for Firefox browser
#driver=webdriver.firefox()  
#driver=webdriver.ie()  

#maximize the window size  
driver.maximize_window()  

#navigate to the url  
driver.get("https://www.google.com/")  

#identify the Google search text box and enter the value  
driver.find_element_by_name("q").send_keys("javatpoint")  

#wait time of 3 seconds
time.sleep(3)  

#click on the Google search button  
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
time.sleep(3)  

#close the browser  
driver.close() 
#success message that the script run successfully
print("sample test case successfully completed")  

import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome('C:/Users/Gaurav Sachdev/Desktop/Code/Python/Script/chromedriver')  # Optional argument, if not specified will search path.
driver.set_page_load_timeout(10)
c=0
t=True
while t==True:
  if(c>20):
    print("Check Internet Connectivity")
    driver.quit()
    exit()
  try:
       driver.get('https://192.168.10.3/connect/PortalMain')
       c+=1
       time.sleep(1)
       username= driver.find_element_by_id('LoginUserPassword_auth_username')
       us='Enter Username'
       pa='Enter Password'
       us=input("Enter Username");
       pa=input("Enter Password");
       username.send_keys(us)
       password= driver.find_element_by_id('LoginUserPassword_auth_password')
       password.send_keys(pa)
       login= driver.find_element_by_id('UserCheck_Login_Button_span')
       login.click()
       time.sleep(2) # Let the user actually see something!
  except:
       print("Retrying...")
       continue
  else:
       break     
driver.quit()

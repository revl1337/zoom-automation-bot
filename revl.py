# Some packages used in this script

import datetime
from selenium import webdriver
import colorama
from colorama import Fore
import time
import schedule

# Messages that get logged to the console upon startup

print(Fore.GREEN + 'Welcome to Revl\'s Zoom Bot!')
time.sleep(2)
print(Fore.GREEN + 'Starting...')

# Webdriver Location & Datetime Keyword

driver =  webdriver.Chrome("") # Double click to run your chrome driver and enter the ChromeDriver Location here (Make sure after your drive location there are two back slashes, Example: C:\\Users\revl\OneDrive\Desktop\MyZoomBot\chromedriver.exe) 
e = datetime.datetime.now()

# Link Credentials

FirstClassTime = "" # Enter the time your first class starts (24-h Clock)
SecondClassTime = "" # Enter the time your second class starts (24-h Clock) 

# Note: If you have more than 2 classes just repeat the process that is above.

main = "" # your main zoom url
french = "" # your second class zoom url

# Join Functions

def LoadMain():
    driver.get(main) # You can add more, Repeat what's been done here for you, if you have more than two classes.
    time.sleep(60) 
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()
def LoadFrench():
    driver.get(french)
    time.sleep(60)
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

# Weekly Timetable

def monday():
    schedule.every().monday.at(FirstClassTime).do(LoadMain()) # As said above, If you have more than 2 classes. Repeat the process done for you.
    schedule.every().monday.at(SecondClassTime).do(LoadFrench()) 
def tuesday():
    schedule.every().tuesday.at(FirstClassTime).do(LoadMain())
    schedule.every().tuesday.at(SecondClassTime).do(LoadFrench())
def wednesday():
    schedule.every().wednesday.at(FirstClassTime).do(LoadMain())
    schedule.every().wednesday.at(SecondClassTime).do(LoadFrench())
def thursday():
    schedule.every().thursday.at(FirstClassTime).do(LoadMain())
    schedule.every().thursday.at(SecondClassTime).do(LoadFrench())
def friday():
    schedule.every().friday.at(FirstClassTime).do(LoadMain())
    schedule.every().friday.at(SecondClassTime).do(LoadFrench())

# Logging to the console What Day it is

day = (e.strftime("%a"))
print(day)
if day=="Mon":
    monday()
elif day=="Tue":
    tuesday() 
elif day=="Wed":
    wednesday()
elif day=="Thu":
    thursday()
elif day=="Fri":
    friday()
else:
    print('It\'s the weekend!')

# Automation of clicking the "Always allow zoom.us to open links of this type"

popup = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div')
popup.click()
print("[BOT] SUCCESSFULLY LOGGED IN & LOADED ZOOM!")
while True:
    schedule.run_pending()
    time.sleep(0.01)

# The End of the script!


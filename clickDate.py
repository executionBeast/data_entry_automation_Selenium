import pyautogui as pg
from time import sleep

date='date25f.tiff'
datef='date25f.tiff'


def locateDate(date):
  sleep(0.2)
  allOcurrence = list(pg.locateAllOnScreen(date))
  print(allOcurrence)
  coordinates = [pg.center(allOcurrence) for allOcurrence in allOcurrence]
  print("Located Date Crrdnate : ",coordinates)
  pg.click(coordinates[0])
  # for coord in coordinates: 
  #   print(f"Image found at: {coord}")

# locateDate()



print("Date is : "+date+"\n")

def clickDate():
  sleep(0.3)
  # dateFrom = pg.locateOnScreen('dateFrom.png',confidence=.1)
  # sleep(1)
  # dateTo = pg.locateOnScreen('dateTo.png',confidence=.1)
  # y = pg.locateOnScreen('date.png',grayscale=True,confidence=.1)

  # pg.click('date.png')
  # sleep(2)
  # pg.click('date6.png')

  #selecting date from

  # print("dateFrom : {} dateTo : {} ".format(dateFrom,"yg"))
  #pg.click('dateFrom.png')
  try:
    pg.click('dateFrom.tiff')
    sleep(0.5)
    # pg.click(date)
    locateDate(date)
    
    sleep(0.4) 
  except all:
    print("date from not filled",all)

  # selecting date to
  try:
    allOcurrence = list(pg.locateAllOnScreen('dateFrom.tiff'))
    coordinates = [pg.center(allOcurrence) for allOcurrence in allOcurrence]
    pg.click(coordinates[1])
    # pg.click('dateTo.tiff')
    sleep(0.5)
    # pg.click('dateTo.tiff')
    # sleep(1.5)
    # pg.click(datef)
    locateDate(date)

  except all:
    print('date to not  filled',all)


# clickDate()


# import random
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from time import sleep
# import pyautogui as pg


# s = Service("chromedriver-linux64/chromedriver")
# driver = webdriver.Chrome(service = s)

# url = "https://poshanabhiyaan.gov.in/login"

# driver.get(url)     #open poshan abhiyan website
# driver.maximize_window()

# sleep(1)

# username = "mow&cd-912612"
# password = "mow&cd-912612"

# userIn =driver.find_element(By.NAME,"username")
# passIn =driver.find_element(By.NAME,"password")
# loginBtn = driver.find_element(By.XPATH,"/html/body/div/div/section/div/div/div/div[1]/div/form/div/div[4]/button")

# while True:
#     try:
#         if userIn.is_displayed():
#             break
        
#     except:
#         print("Login Field is not loaded!")
#     sleep(0.5)

# userIn.send_keys(username)
# sleep(0.1)
# passIn.send_keys(password)
# sleep(0.5)
# loginBtn.click()
# sleep(8)
# fromDateChangeScript="document.getElementsByName('SelectDateFrom').forEach(e=>{e.click();});"
# toDateChangeScript="document.getElementsByName('SelectDateTo').forEach(e=>{e.click();});" 

# # driver.execute_script("alert('Hello')")
# driver.execute_script(fromDateChangeScript)
# sleep(10)
# driver.execute_script(toDateChangeScript)



# sleep(120)




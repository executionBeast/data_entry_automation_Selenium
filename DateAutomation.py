













# import random
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep

# # Chrome options to disable automation flags
# chrome_options = webdriver.ChromeOptions()
# prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# chrome_options.add_experimental_option("prefs", prefs)

# # WebDriver setup
# s = Service("chromedriver-linux64/chromedriver")
# driver = webdriver.Chrome(service=s, options=chrome_options)

# # Open the website
# url = "https://poshanabhiyaan.gov.in/login"
# driver.get(url)
# driver.maximize_window()

# #---------------------Login Logic----------------------------------------
# username = "mow&cd-912614"
# password = "mow&cd-912614"

# # Find login elements and login
# userIn = driver.find_element(By.NAME, "username")
# passIn = driver.find_element(By.NAME, "password")
# loginBtn = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/div/div[1]/div/form/div/div[4]/button")

# # Wait for login fields to be visible
# while True:
#     try:
#         if userIn.is_displayed():
#             break
#     except:
#         print("Login Fields are not loaded")
#         sleep(0.5)
# # <input class="date_range_input" type="date" placeholder="Select Date" name="SelectDateFrom" min="2024-09-05" max="2024-09-08" value>
# # Enter credentials and login
# userIn.send_keys(username)
# sleep(0.1)
# passIn.send_keys(password)
# sleep(0.1)
# loginBtn.click()

# #---------------------Date Selection Logic-----------------------------

# # Wait for the page containing the date input to load
# while True:
#     try:
#         if driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/form/div[1]/div/div[1]/div/div/input").is_displayed():
#             print("Date input is loaded!")
#             break
#     except:
#         print("Page not loaded yet!")
#         sleep(0.5)

# # Function to automate date selection
# def select_date_range(date_from, date_to):
#     try:
#         # Step 1: Select the DateFrom field using JavaScript
#         date_from_input = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.NAME, "SelectDateFrom"))
#         )
#         print("DateFrom input is loaded!")
        
#         # Set DateFrom value using JavaScript
#         driver.execute_script(f"arguments[0].value = '{date_from}';", date_from_input)
#         print(f"DateFrom '{date_from}' has been selected.")

#         # Step 2: Trigger any JavaScript events or updates
#         driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_from_input)
#         print("DateFrom 'change' event triggered!")

#         # Step 3: Wait for DateTo field to become enabled
#         date_to_input = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.NAME, "SelectDateTo"))
#         )
#         print("DateTo input is loaded!")

#         # Wait until DateTo is enabled
#         WebDriverWait(driver, 20).until(
#             lambda driver: date_to_input.is_enabled()
#         )
#         print("DateTo input is now enabled!")

#         # Step 4: Set DateTo value using JavaScript
#         driver.execute_script(f"arguments[0].value = '{date_to}';", date_to_input)
#         driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_to_input)
#         print(f"DateTo '{date_to}' has been selected.")
        
#     except Exception as e:
#         print(f"Error selecting date range: {e}")

# # Usage example
# select_date_range("2024-09-06", "2024-09-06")
# # Call the function to automate date selection (example date: 2024-09-01)
# # select_date("2024-09-06")

# # Sleep for a while to observe the changes
# sleep(120)

# # Close the browser
# # driver.quit()

# print("Date selection automated successfully!")


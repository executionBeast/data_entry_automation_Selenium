import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from time import sleep
import pyautogui as pg
from clickDate import clickDate

visited = ['Select a AWC']

#visited = ['Select a AWC', 'AKHAINI(Shyama)', 'BABRAPUR(Chinta)', 'BABRAPUR(Shakuntla)', 'BACHAPAR(Chandrakanta)', 'BACHAPAR(Meera)', 'BACHAPAR(Santosh)', 'BACHAPAR(Vidyawati)', 'BADASARI(Indu Tiwari)', 'BAGHA(Sarita)', 'BAHERI (POONAM)', 'BAHERI(Saroj)', 'BANKATA(Gayatri)', 'BANKATA(Gudiya)', 'BELAHI(Meena)', 'BELAONA(Arti)', 'BHABHNAULI(Champa)', 'BHUDADIH(Geeta)', 'BHUDADIH(Suman)', 'BICHIBOJH(Lalti)', 'BISHHAR(Mamta)', 'BISHHAR(pushpa)', 'CHACHARI(Nilam)', 'CHACHARI(Urmila)', 'CHAKBAHADUN(Geeta)', 'CHAKBAHADUN(Munni)', 'CHAKJALALPUR(Seema)', 'CHAKJIYA(Punam)', 'CHAKMOTI(Reema)', 'CHAKRA(Sanjita)', 'CHAKUJIYAR(Panna)', 'CHAKUSHAULI(Asha)', 'CHAKUSHAULI(Sanju)', 'CHARWA BARWA(Dewanti)', 'CHARWA BARWA(Habibunisa)', 'CHARWA BARWA(Meena)', 'CHARWA BARWA(Sona Devi)', 'CHARWA BARWA(Tara)', 'CHITUPUR(Rajkumari)', 'CHOTIVISHAHAR(Manju)', 'DAKINGANJ', 'DHADNSARA(Nilam)', 'DHANEJA(Rinku)', 'DHANEJA(Vijyanti)', 'DOBHWA(Lalsa)', 'Doghara (Seema)', 'Doghara(Neetu)', 'EKAIL(Gangotri)', 'EKAIL(Geeta)', 'FIROJPUR(Shailkumari)', 'FIROJPUR(Urmila)', 'GADMALPUR(Babita)', 'GADMALPUR(Manki)', 'GADMALPUR(Usha)', 'GAURAMADANPURA(Aarti)', 'GAURAMADANPURA(Vimla)', 'GAURI(Kiran)', 'GAURI(Omlata)', 'GAURI(Suman)', 'GAURNIYA(Mansha)', 'GODWARA(Indu Yadav)', 'GOPALPUR(Punam)', 'HARIPUR(Ambika)', 'HARIPUR(Sharda)', 'JAGDARA(Durgaji Tiwari)', 'JAGDARA(Tara)', 'JANUWAL(Geeta)', 'JANUWAL(Kismat)', 'JETHWAR(Durgawati)', 'JETHWAR(Sunanda)', 'JIMICHAK(phulwanti)', 'JOGESHARA(Munni)', 'KACHILA(Gyanti)', 'KADSAR(Gyanti)', 'KAITHAULI(Maya)', 'KAITHAULI(Radhika)', 'KALYADDEHRA(Chandrawati)', 'KALYADDEHRA(Sushila)', 'KHABASPUR(Nirmala)', 'KHADRSHARA(Anju)', 'KHADRSHARA(Savitri)', 'KHADRSHARA(Subhawati)', 'KHADRSHARA(Urmila)', 'KHAIRACHAK(Sangeeta)', 'KHEJURI P.S 1(Nisha)', 'KHEJURI P.S.2(Kanti)', 'KHEJURI(Usha)', 'KHEJURIP.S.2(Munni)', 'KHEJURIP.S.3(Sunita)', 'KHERACHAK(Suman)', 'KIKODARA(Manju)', 'KIKODARA(Tapasya)', 'KIKODHA(Meera)', 'KUDHI(Kunti)', 'LAKHNAPAR(Gayatri)', 'LEDUHI(Krishna)', 'MAHULANPAR(Meera)', 'MAHULANPAR(Rekha)', 'MASUMPUR(Afrin)', 'MASUMPUR(Amravati)', 'MASUMPUR(Saroj)', 'MASUMPUR(Sunaina)', 'MEULI(Manju)', 'MEULI(Nirmala)', 'MISHRAULI(Anjana)', 'MISHRAULI(Rinku)', 'MISHRAULI(Shubhawati)', 'MUDERA(Kavitaa)', 'MUJHI(Usha)', 'NAHILAPAR', 'NANHUL(Nayantara)', 'NANHUL(Usha)', 'PAHRAJPUR(Geeta)', 'PAKADI((Rita Singh)', 'PAKADI(Dropadi)', 'PAKADI(Kanaklata)', 'PAKADI(Rita Devi)', 'PAKADI(Urmila Gupta)', 'PAKADI(Urmila devi)', 'PAKADI(Usha)', 'PANDAH(Meena Rai)', 'PRASHADPUR(Gyanti)', 'PRASHADPUR(Sheela)', 'PUR(Asha)', 'PUR(Meera)', 'PUR(Mina)', 'PUR(Pinki)', 'PUR(Poonam)', 'PUR(Sanju)', 'PUR(Sunita)', 'RAKSHA(Meena)', 'RAMAPAR(Kaanti)', 'RAMAPAR(Umraavati)', 'RATSHI(Chinta)', 'RATSHI(Sheela)', 'RUPWAR(Reeta)', 'RUPWAR(Seema)', 'RUPWAR(Usha)', 'SAHULAI(M)(Sureman)', 'SAHULAI(Manju Yadav)']
chrome_options = webdriver.ChromeOptions()
prefs = {"credentials_enable_service": False,"profile.password_manager_enabled": False}
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_experimental_option("prefs",prefs)


s = Service("chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service = s, options=chrome_options)

url = "https://poshanabhiyaan.gov.in/login"

driver.get(url)     #open poshan abhiyan website
driver.maximize_window()

#---------------------Login Logic----------------------------------------
username = "mow&cd-912614"
password = "mow&cd-912614"

userIn =driver.find_element(By.NAME,"username")
passIn =driver.find_element(By.NAME,"password")
loginBtn = driver.find_element(By.XPATH,"/html/body/div/div/section/div/div/div/div[1]/div/form/div/div[4]/button")

while True:
    try:
        if userIn.is_displayed():
            break
        
    except:
        print("Login Fields are not loaded")
        sleep(0.5)

userIn.send_keys(username)
sleep(0.1)
passIn.send_keys(password)
sleep(0.1)
loginBtn.click()
#-------------------------------/Login Logic---------------------------
#driver.find_element(By.NAME,"username")

while True:
    try:
        if driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/form/div[1]/div/div[1]/div/div/input").is_displayed() and driver.find_element(By.NAME,"EnterDescription").is_displayed :
            sleep(0.2)
            print("page loaded!")
            break
    except:
        print("Page not Loaded!")
        sleep(0.5)

Theme = Select(driver.find_element(By.NAME,"SelectTheme"))
Activity = Select(driver.find_element(By.NAME,"SelectActivity"))
Level = Select(driver.find_element(By.NAME,"SelectLevel"))




def Automate(visited,closeDriver):
#---------------selecting theme, activity, level-----------------------------------

    
    # sleep(0.1)
    Theme.select_by_index('3')
    # sleep(0.3)

    clickDate()  #click date 06/09/2023
    # sleep(0.3)

    Level.select_by_value('5')   #AWC   ise select karte hi AWS selection khul jaayega 
    sleep(0.8)


    

    
    #------------------------------------Selecting Aanganwadi Logic---------------------------------------------------------------------
    while True:
        try:
            if driver.find_element(By.NAME,"awc_center").find_elements(By.TAG_NAME,"option"):
                sleep(0.2)
                print("awc input is visible")
                break
        except:
            print("awc input not loaded")
            sleep(0.1)

    AWC = driver.find_element(By.NAME,"awc_center")  #iteratable aanganwadi 
    allAWC = AWC.find_elements(By.TAG_NAME,"option")

    for awc in allAWC:
        if awc.get_attribute("text") in visited:
            continue
        if awc.get_attribute("text") =='pandah(Sonamati)':  
                closeDriver = True
        visited.append(awc.get_attribute("text"))
        awc.click()    #selecting the awc
        sleep(0.1)
        print(visited)
        break
            

    #------------------------------------/Selecting Aanganwadi Logic---------------------------------------------------------------------
    
    # CountActivity = driver.find_element(By.NAME,"SelectActivity")
    # allAct = CountActivity.find_elements(By.TAG_NAME,"option")
    # for act in allAct:
    #     print(act.get_attribute('value'))
    #     print(act)
    
    while True:
        try:
            if driver.find_element(By.NAME,"SelectActivity").find_elements(By.TAG_NAME,"option"):
                sleep(0.2)
                break
        except:
            print("Activity Option not Loaded!")
            sleep(0.2)

    Activity.select_by_value('18')
    sleep(0.1) 

    AdultMale = driver.find_element(By.NAME,"CountAdultMale")
    AdultFemale = driver.find_element(By.NAME,"CountAdultFemale")
    ChildMale = driver.find_element(By.NAME,"CountChildMale")
    ChildFemale = driver.find_element(By.NAME,"CountChildFemale")

    AdultMale.clear()
    AdultMale.send_keys(random.randint(15,50))
    sleep(0.1)
    AdultFemale.clear()
    AdultFemale.send_keys(random.randint(15,55))
    sleep(0.1)
    ChildMale.clear()
    ChildMale.send_keys(random.randint(11,48))
    sleep(0.1)
    ChildFemale.clear()
    ChildFemale.send_keys(random.randint(13,50))

    sleep(0.5)
    pg.scroll(-4)
    pg.click('description.png')
    sleep(0.1)
    driver.execute_script("document.querySelector('.submit_button_box button').click();") #click submit
    while True:
        try:
            if driver.find_elements(By.CLASS_NAME, "form-submitted-section"):
                print("Successfully Submitted")
                sleep(2)
                break
        except:
            print("Form Submission is ongoing!")
            sleep(0.5)


    sleep(1)
    pg.scroll(5)
    if closeDriver:
        print('Closing Chrome Driver....!')
        driver.close()

    print("_______________ Everything Working fine! __________________")


#------------------------------------------------------------------------------------

for i in range(178):
    closeDriver=False
    Automate(visited,closeDriver)
    if closeDriver:
        break
        
exit()


# sleep(0.5)

#--------------Selecting Aanganwadii----------------------------------

# DateFrom = driver.find_element(By.NAME,"SelectDateFrom")
# sleep(0.2)
# DateTo = driver.find_element(By.NAME,"SelectDateTo")



# clickDate()  #click date 06/09/2023
# sleep(1)

# AdultMale = driver.find_element(By.NAME,"CountAdultMale")
# AdultFemale = driver.find_element(By.NAME,"CountAdultFemale")
# ChildMale = driver.find_element(By.NAME,"CountChildMale")
# ChildFemale = driver.find_element(By.NAME,"CountChildFemale")

# SubmitBtn = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div/div/div/div/form/div[4]/div/div[2]/div/div[2]/button")



    
#     #--------------------Entering Male Female number------------------
#     # CountAdultMale = random.randint(9,18)
#     # CountAdultFemale = random.randint(8,19)
#     # CountChildMale = random.randint(9,18)
#     # CountChildFemale = random.randint(9,20)

#     AdultMale.send_keys(random.randint(9,18))
#     sleep(0.2)
#     AdultFemale.send_keys(random.randint(9,20))
#     sleep(0.2)
#     ChildMale.send_keys(random.randint(9,19))
#     sleep(0.2)
#     ChildFemale.send_keys(random.randint(9,22))
    
#     sleep(0.3)
#     # SubmitBtn.click()
#     print("Aanganwadi is {}".format(awc.get_attribute("text")))
#     print("Successfully Submited!")
#     sleep(60)


# AdultMale.send_keys(random.randint(15,30))
# sleep(0.5)
# AdultFemale.send_keys(random.randint(20,38))
# sleep(0.5)
# ChildMale.send_keys(random.randint(14,30))
# sleep(0.5)
# ChildFemale.send_keys(random.randint(20,38))

# sleep(0.5)
# pg.scroll(-4)
# pg.click('description.png')
# sleep(1)
# driver.execute_script("document.querySelector('.submit_button_box button').click();") #click submit
# sleep(10)
# pg.scroll(4)

# SubmitBtn.click()
# print("Aanganwadi is {}".format(awc.get_attribute("text")))
# print("Successfully Submited!")

sleep(20)
# print("_______________ Everything Working fine! __________________")

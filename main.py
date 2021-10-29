from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from threading import Thread
import time

def stream(url:str, acc:list):
    while True:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--log-level=3")

        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        driver.find_element_by_css_selector("div.Root.encore-dark-theme div.Root__top-container:nth-child(2) div.Root__top-bar header.Hs_M1kkmTOjAAOogsztS.s9ADdgllHepMRX_Jyl_p:nth-child(1) div:nth-child(4) > button.MgL79SorehxR01FG_x8G.t5cpZkLic_tfF1qAxBiu:nth-child(2)").click()
        time.sleep(3)
        driver.find_element_by_xpath("//input[@id='login-username']").send_keys(acc[0]) # ввод почты
        driver.find_element_by_xpath("//input[@id='login-password']").send_keys(acc[1]) # ввод пароля
        driver.find_element_by_xpath("//button[@id='login-button']").click() # нажатие на кнопку входа
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//body/div[@id='main']/div[1]/div[2]/div[3]/main[1]/div[2]/div[2]/div[1]/div[1]/div[2]/section[1]/div[3]/div[1]/button[1]"))).click() # я не ебу зачем так сложно но без этого не работает
        driver.find_element_by_id("onetrust-close-btn-container").click()
        time.sleep(27)
        driver.close()

def main():
    track_url = input("Track URL: ")

    with open("accounts.txt", "r") as f:
        accounts = f.readlines()

    for acc in accounts:
        acc = acc.split(":") # разделение данных на почту и пароль
        Thread(target=stream, args=(track_url, acc)).start()
        time.sleep(3)

if __name__ == "__main__":
    main()
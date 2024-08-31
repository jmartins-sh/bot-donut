from faker import Faker
from faker.providers import internet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

import random
import csv
import time
import sys


def generate_email():
    fake = Faker()
    fake.add_provider(internet)
    user_name = fake.user_name()
    domain = "@tuamaeaquelaursa.com"
    random_number = random.randint(18, 80)
    return f"{user_name}{random_number}{domain}"


def run(referral_link, emails_to_create):
    proxy = "52.67.10.183:3128"
    agent_name = (
        "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
    )
    options = Options()

    webdriver.DesiredCapabilities.CHROME["proxy"] = {
        "httpProxy": proxy,
        "ftpProxy": proxy,
        "sslProxy": proxy,
        "proxyType": "MANUAL",
    }

    webdriver.DesiredCapabilities.CHROME["acceptSslCerts"] = True

    # options.add_argument(f"--proxy-server={proxy}")
    options.add_argument(f"--user-agent={agent_name}")
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    csv_file_headers = ["dumb_email", "password", referral_link]

    with open("./test.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(csv_file_headers)

        sign_up_xpath = "//html//body//div[@id='__next']//div[@class='c-PJLV c-PJLV-ikRbgih-css']//div[@class='c-PJLV c-PJLV-ikGFHpk-css']//main//div//div//div[@class='c-dhzjXW c-dhzjXW-iiqjHSX-css']//button"

        form_xpah = "//html//body//div"

        btn = "//button[@class='c-ggLWnt c-ggLWnt-drNcRn-color-secondary c-ggLWnt-fbplYV-size-medium c-ggLWnt-fGHEql-fullWidth-true c-ggLWnt-cbiXQb-cv c-ggLWnt-ieLJojA-css']"

        for i in range(emails_to_create):
            print(f"Processando {i+1} / {emails_to_create} emails...")
            driver.get(referral_link)

            button = driver.find_element(By.XPATH, sign_up_xpath)

            ActionChains(driver).click(button).perform()

            dumb_email = generate_email()
            dumb_password = "102030"

            driver.find_element(By.CLASS_NAME, "c-eePeRJ-iloVUTh-css").send_keys(
                dumb_email
            )  # email field
            driver.find_element(By.CLASS_NAME, "c-eePeRJ-ijoJtkc-css").send_keys(
                dumb_password
            )  # pass field
            driver.find_element(By.CLASS_NAME, "c-eePeRJ-ijoJtkc-css").send_keys(
                dumb_password
            )  # re type pass field

            btn_continue = driver.find_element(
                By.XPATH,
                btn,
            )

            btn_continue.click()

            if (i + 1) % random.randint(5, 9) == 0:
                time.sleep(random.randint(60, 90))

            writer.writerow([dumb_email, dumb_password, "OK"])
            print("OK")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Necessario informar quantidade de emails e link de referral")
        raise

    referral_link = sys.argv[1]
    emails_to_create = int(sys.argv[2])
    print(
        f"Iniciando o processamento de {emails_to_create} emails para o link: {referral_link}"
    )
    run(referral_link, emails_to_create)

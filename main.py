from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3921003223&f_AL=true&f_WT=2&geoId=101165590&keywords=data%20analyst&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true")

sign_in = driver.find_element(By.CLASS_NAME, value="nav__button-secondary")
sign_in.click()

time.sleep(5)
username = driver.find_element(By.ID, "username")
username.send_keys("")

password = driver.find_element(By.ID, "password")
password.send_keys("")

sign_in_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
sign_in_button.click()

time.sleep(2)
job_list = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container li")

for job in job_list:
    [job.click() for job in job_list]






# time.sleep(5)
# easy_apply = driver.find_element(By.ID, "ember50")
# easy_apply.click()
#
# next = driver.find_element(By.CSS_SELECTOR, ".justify-flex-end button")
# next.click()
#
# time.sleep(3)
# review = driver.find_element(By.CSS_SELECTOR, "button.artdeco-button--primary")
# review.click()
#
# time.sleep(3)
# submit_application = driver.find_element(By.CSS_SELECTOR, "button.artdeco-button--primary")
# submit_application.click()
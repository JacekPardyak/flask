from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# instantiate options for Chrome
options = webdriver.ChromeOptions()

# run browser in headless mode
options.add_argument('--headless=new')


# instantiate Chrome WebDriver with options
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# URL of the web page to scrape
url = 'https://ofertypracy.edu.pl/?filter%5Brspo.voivodeship_id%5D=18&sort=-published_at&per_page=50&search=1&page=1'
driver.get(url)

xpath = '//*[@id="app"]/main/div[1]/div[2]/div/div/div[1]/div/span'
total = driver.find_elements(By.XPATH, xpath)[0].text
import re
total = int(re.sub('\D', '', total))
# open the specified URL in the browser

# find elements by class name 'product-name'
job_ids = []
job_tts = []
job_pls = []
for i in range(50):
  job_id = driver.find_elements(By.XPATH, f'//*[@id="app"]/main/div[1]/div[3]/div/div/a[{1 + i}]/div/div[1]/div/div[1]/div/div')
  job_ids = job_ids + [job_id[0].text]
  job_tt = driver.find_elements(By.XPATH, f'//*[@id="app"]/main/div[1]/div[3]/div/div/a[{1 + i}]/div/div[1]/div/div[1]/h3')
  job_tts = job_tts + [job_tt[0].text]
  try:
    job_pl = driver.find_elements(By.XPATH, f'//*[@id="app"]/main/div[1]/div[3]/div/div/a[{1 + i}]/div/div[1]/div/div[2]/div[3]/div[2]')
    job_pls = job_pls + [job_pl[0].text]
  except IndexError:
    job_pl = driver.find_elements(By.XPATH, f'//*[@id="app"]/main/div[1]/div[3]/div/div/a[{1 + i}]/div/div[1]/div/div[2]/div[2]/div[2]')
    job_pls = job_pls + [job_pl[0].text]
import pandas as pd
df = pd.DataFrame({
    'job_ids': job_ids,
    'job_tts': job_tts,
    'job_pls': job_pls
})
# close the browser
driver.quit()

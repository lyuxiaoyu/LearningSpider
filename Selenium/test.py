from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chromedriver_path = r'C:\Program Files\Python36\Scripts\chromedriver.exe'

driver = webdriver.Chrome(executable_path = chromedriver_path, chrome_options = chrome_options);

driver.get('http://www.baidu.com');
print(driver.title)

driver.get('https://www.bilibili.com/');
print(driver.page_source)

driver.close();

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time

chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
chromedriver_path = r'C:\Program Files\Python36\Scripts\chromedriver.exe'
driver = webdriver.Chrome(executable_path = chromedriver_path, chrome_options = chrome_options);

try:
    with open('zhihuCookies', 'r') as fr:  
        cookies = json.load(fr);
        driver.get(r'https://www.zhihu.com');

        for c in cookies:
            driver.add_cookie(c);
        
        driver.get(r'https://www.zhihu.com');
        time.sleep(3);
#        print(driver.page_source);
        
except:

    driver.get(r'https://www.zhihu.com');
    print(driver.title);

    transLoginButton = driver.find_element_by_xpath(r"//span[@data-reactid='93']");
    transLoginButton.click()

    username = driver.find_element_by_xpath(r"//input[@name='username']");
    username.send_keys('15988842170');

    password = driver.find_element_by_xpath(r"//input[@name='password']");
    password.send_keys('1234asdf')

    loginButton = driver.find_element_by_xpath(r"//button[@type='submit']");
    loginButton.click();
    
    time.sleep(3);
    cookies = driver.get_cookies();
    
    with open('zhihuCookies', 'w') as fw:  
       json.dump(cookies, fw);
       
driver.close();


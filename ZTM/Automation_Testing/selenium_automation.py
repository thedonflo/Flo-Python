from selenium import webdriver

#We will be using Selenium Easy Website(https://www.seleniumeasy.com/) as a playground for testing

chrome_browser = webdriver.Chrome('./chromedriver.exe')           #Make sure your desired web driver is within location

# print(chrome_browser)
chrome_browser.maximize_window()                                #Launch chrome browser in maximimum window

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

'Selenium Easy Demo' in chrome_browser.title                #Verify we are on the correct website by checking the title
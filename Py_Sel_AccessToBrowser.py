from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary)
#driver.get('http://seleniumhq.org/')
driver.get('http://localhost:920/')


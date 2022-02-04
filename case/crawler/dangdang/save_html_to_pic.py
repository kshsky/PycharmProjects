from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url='https://www.cnblogs.com/subconscious/p/5058741.html'
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "normal"
driver = webdriver.Chrome(executable_path='D:\program\PycharmProjects\dataFile\scrapy\chromedriver.exe',
                               desired_capabilities=desired_capabilities)

driver.get(url)
driver.get_screenshot_as_file("screenshot.png")
import time, os
from urllib.parse import urlparse
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options, executable_path='./geckodriver')
# driver = None
def login(email, password):
    url = "https://www.instagram.com/accounts/login/"
    driver.get(url)

    # waiting to load website
    time.sleep(2)

    username_element = driver.find_element_by_xpath('//*[@name="username"]')
    password_element = driver.find_element_by_xpath('//*[@name="password"]')

    username_element.send_keys(email)
    password_element.send_keys(password)

    password_element.send_keys(Keys.ENTER)
    time.sleep(2)



def get_image(url, output_location):

    driver.get(url)
    time.sleep(1)

    url = url.split('/')[-2]
    file_name = "{0}.jpg".format(url)

    image_element = driver.find_element_by_class_name("FFVAD")
    image_url = image_element.get_attribute("src")

    with open(output_location + file_name, 'wb') as output:
        output.write(urlopen(image_url).read())

# login()
# get_image("https://www.instagram.com/p/Bp7MUwuAB4QNWhzgizZDOp-V8EEBrAkB3kqA5E0/", "image1.jpg")


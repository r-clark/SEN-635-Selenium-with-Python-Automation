__Author__ = 'r-clark'



from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# global variables
login_id = '**********'
passwd = '************'
search_1 = 'selenium testing with python'

# create instance of webdriver for chrome browser
driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.set_page_load_timeout(30)

# navigate to webpage
driver.get(
    'https://www.amazon.com/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.'
    'assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%'
    '2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2'
    '.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net'
    '%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.'
    '0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%'
    '3Dnav_ya_signin&switch_account=')

# maximize window for test
driver.maximize_window()

# create instance of WebDriverWait
wait = WebDriverWait(driver, 10)

# create instance of ActionChains
actions = ActionChains(driver)

# have selenium wait 5 seconds before executing next line of code
driver.implicitly_wait(5)

# find the email box and insert login id
driver.find_element_by_id('ap_email').send_keys(login_id)

# submit the login id
driver.find_element_by_id('continue').submit()

# take picture of login
driver.get_screenshot_as_file('C:\\Selenium\\python\\Screenshots\\'
                              'amazon_login1.png')
driver.implicitly_wait(5)

# find the password box and insert password and submit credentials
driver.find_element_by_id('ap_password').send_keys(passwd)
driver.implicitly_wait(3)

# submit login and password credentials
driver.find_element_by_id('signInSubmit').submit()

# take screen shot of action
driver.get_screenshot_as_file('C:\\Selenium\\python\\Screenshots\\'
                              'amazon_login_w_passwd.png')
driver.implicitly_wait(3)

# find search box and isert search criteria and submit
driver.find_element_by_id('twotabsearchtextbox').send_keys(search_1)
driver.get_screenshot_as_file('.\\Screenshots\\amazon_search.png')
driver.find_element_by_class_name('nav-input').submit()
driver.implicitly_wait(3)

# find 'Test-Driven Web Development with Python' and click link
driver.find_element_by_xpath('//*[@id="result_0"]/div/div[3]/div[1]/a/h2').click()
driver.get_screenshot_as_file('C:\\Selenium\\python\\Screenshots\\'
                              'amazon_click_book.png')
driver.implicitly_wait(3)

# click on paperback version of book
driver.find_element_by_xpath('//*[@id="mediaTab_heading_1"]/a/span/div[1]/span').click()
driver.get_screenshot_as_file('.C:\\Selenium\\python\\Screenshots\\'
                              'amazon_select_paperback.png')
driver.implicitly_wait(3)

# add book to cart
driver.find_element_by_id('add-to-cart-button').submit()

# navigate to cart
driver.find_element_by_xpath('//*[@id="nav-cart"]').click()
driver.get_screenshot_as_file('.\\Screenshots\\amazon_show_cart.png')

# delete item from cart
driver.find_element_by_xpath('//*[@id="activeCartViewForm"]/div[2]/div/div[4]/div/div[1]/div/div/div[2]'
                             '/div/span[1]/span/input').click()
driver.get_screenshot_as_file('C:\\python\\Screenshots\\'
                              'amazon_delete_cart.png')

# navigate to drop down menu to sign out
drop_down_menu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
actions.move_to_element(drop_down_menu).perform()
driver.get_screenshot_as_file('C:\\Selenium\\python\\Screenshots\\'
                              'amazon_show_dropdown.png')
driver.implicitly_wait(3)

# click sign-out
wait.until(EC.visibility_of_element_located(( By.ID, 'nav-item-signout-sa',))).click()
driver.get_screenshot_as_file('C:\\Selenium\\python\\Screenshots\\'
                              'amazon_show_click_signout.png')
driver.implicitly_wait(15)

# exit program
driver.quit()

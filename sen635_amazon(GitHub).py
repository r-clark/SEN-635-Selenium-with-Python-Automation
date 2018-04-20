# -*- coding: utf-8 -*-
__Author__ = 'r-clark, b-nieman, b-cashman'
 
import os 
import sys
import time 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

banner = """
-------------------------------------------------------
-------------------------------------------------------

███████╗███████╗███╗   ██╗     ██████╗ ██████╗ ███████╗
██╔════╝██╔════╝████╗  ██║    ██╔════╝ ╚════██╗██╔════╝
███████╗█████╗  ██╔██╗ ██║    ███████╗  █████╔╝███████╗
╚════██║██╔══╝  ██║╚██╗██║    ██╔═══██╗ ╚═══██╗╚════██║
███████║███████╗██║ ╚████║    ╚██████╔╝██████╔╝███████║
╚══════╝╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚═════╝ ╚══════╝

		Automated Testing by: 
		- Brett Nieman
		- Richard Clark
		- Benjamin Cashman
-------------------------------------------------------
-------------------------------------------------------
"""	
baseUrl = "https://www.amazon.com/"
#determine operating system 
opSys = sys.platform
clear = '' 
if "linux" in opSys or "os" in opSys or "mac" in opSys:
	clear = 'clear'
else: 
	clear = 'cls'

os.system(clear)
print(banner)
print("STARTING AUTOMATED TESTING ON: ")
print(baseUrl + "\n")

#determining client browser -- default set to Firefox
try:
	driver = webdriver.Firefox()
except:
	driver = webdriver.Chrome("C:\\Users\\ricks\PycharmProjects\\Selenium\\chromedriver.exe")

# global variables 
login_id = '***********' 
passwd = '*************' 
search_1 = 'selenium testing with python' 
bookTitle = ''
passed = 0
failed = 0
errors = 0

# create instance of ActionChains 
#actions = ActionChains(driver) 
 
# have selenium wait 5 seconds before executing next line of code 
driver.implicitly_wait(3) 

def testCase1():# log in 
	driver.get(baseUrl)
	loginCount = 0
	try: 
		driver.find_element_by_id("nav-link-accountList").click()
		loginCount += 1
		driver.find_element_by_id('ap_email').send_keys(login_id)
		loginCount += 1
		driver.find_element_by_id("continue").click()
		loginCount += 1
		driver.find_element_by_id('ap_password').send_keys(passwd)
		loginCount += 1
		driver.find_element_by_id('signInSubmit').click() 
		loginCount += 1
		loginName = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div/a[2]/span[1]")
		loginName = loginName.text[7:]
		if loginCount == 5 and loginName == "SeleniumTest":
		    print("[P] TC-1  PASSED - Log in to Amazon")
		    print("                   --> Logged in as: " + "'" + loginName + "'")
		    global passed 
		    passed += 1 
		else:
		    print("[F] TC-1  FAILED - Log in to Amazon")
		    global failed 
		    failed += 1 
	except:
	    print("[E] TC-1  ERROR  - Log in to Amazon")
	    global errors 
	    errors += 1 

def testCase2():# search for item to view
	try: 
		driver.find_element_by_id('twotabsearchtextbox').send_keys(search_1) 
		driver.find_element_by_class_name('nav-input').click() 
		selectedBook = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[1]/div/div/div/div[2]/div[1]/div[1]/a/h2')
		selectedTitle = selectedBook.text
		selectedBook.click()
		global bookTitle
		bookTitle = driver.find_element_by_id("productTitle").text 
		if selectedTitle == bookTitle:
		    print("[P] TC-2  PASSED - Search for item to view")
		    global passed 
		    passed += 1 
		else:
		    print("[F] TC-2  FAILED - Search for item to view")
		    global failed 
		    failed += 1 
	except:
	    print("[E] TC-2  ERROR  - Search for item to view")
	    global errors 
	    errors += 1 

def testCase3():# add item to cart 
	try: 
		bookTitle = driver.find_element_by_id("productTitle").text
		try: 
			driver.find_element_by_xpath('//*[@id="a-autoid-3-announce"]').click()#select paperback
		except:
			pass
		cartPre = driver.find_element_by_id("nav-cart-count").text
		driver.find_element_by_id('add-to-cart-button').click() 
		addedToCart = driver.find_element_by_class_name("a-size-medium.a-text-bold").text
		cartPost = driver.find_element_by_id("nav-cart-count").text
		cartCount = int(cartPost) - int(cartPre)
		if addedToCart == "Added to Cart" and cartCount == 1:
		    print("[P] TC-3  PASSED - Add item to cart")
		    global passed 
		    passed += 1 
		else:
		    print("[F] TC-3  FAILED - Add item to cart")
		    global failed 
		    failed += 1 
	except:
	    print("[E] TC-3  ERROR  - Add item to cart")
	    global errors 
	    errors += 1 

def testCase4():# view cart and confirm correct items exist 
	try: 
		driver.find_element_by_id("nav-cart").click()
		cartItem = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[4]/div/div[2]/div[4]/form/div[2]/div/div[4]/div/div[1]/div/div/div[2]/ul/li[1]/span/a/span").text
		global bookTitle
		if cartItem == bookTitle:
		    print("[P] TC-4  PASSED - View cart for correct item")
		    global passed 
		    passed += 1 
		else:
		    print("[F] TC-4  FAILED - View cart for correct item")
		    global failed 
		    failed += 1 
	except:
	    print("[E] TC-4  ERROR  - View cart for correct item")
	    global errors 
	    errors += 1 

def testCase5():# remove item from cart 
	try: 
		driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[4]/div/div[2]/div[4]/form/div[2]/div/div[4]/div/div[1]/div/div/div[2]/div/span[1]/span/input").click()
		time.sleep(1)
		empty = driver.find_element_by_class_name("a-row.sc-cart-header").text
		price = driver.find_element_by_id("sc-subtotal-amount-activecart").text
		if empty == "Your Shopping Cart is empty." and price == "$0.00":
		    print("[P] TC-5  PASSED - Remove item from cart")
		    global passed 
		    passed += 1 
		else:
		    print("[F] TC-5  FAILED - Remove item from cart")
		    global failed 
		    failed += 1 
	except:
	    print("[E] TC-5  ERROR  - Remove item from cart")
	    global errors 
	    errors += 1 

def testCase6():# return to home page -- confirm cart is empty
	try: 
		driver.find_element_by_id("nav-logo").click()
		profileCard = driver.find_element_by_class_name("hud-profilecard-name")
		profileText = profileCard.text
		cartCount = driver.find_element_by_id("nav-cart-count").text
		if profileCard and profileText == "Hi, SeleniumTest" and cartCount == "0":
		    print("[P] TC-6  PASSED - Return home and verify empty cart")
		    global passed 
		    passed += 1 
		else:
		    print("[F] TC-6  FAILED - Return home and verify empty cart")
		    global failed 
		    failed += 1 
	except:
	    print("[E] TC-6  ERROR  - Return home and verify empty cart")
	    global errors 
	    errors += 1 

def testCase7():# log out 
	try: 
		drop_down_menu = driver.find_element_by_id('nav-link-accountList') 
		logOut = ActionChains(driver).move_to_element(drop_down_menu)
		logOut.perform()
		time.sleep(1)
		driver.find_element_by_id("nav-item-signout-sa").click()
		driver.get(baseUrl)
		signIn = driver.find_element_by_id("nav-link-accountList").text
		if "Hello. Sign in" in signIn:
		    print("[P] TC-7  PASSED - Log out")
		    global passed 
		    passed += 1 
		else:
		    print("[F] TC-7  FAILED - Log out")
		    global failed 
		    failed += 1 
	except:
	    print("[E] TC-7  ERROR  - Log out")
	    global errors 
	    errors += 1 
		
testsDict = {"1" : testCase1, "2" : testCase2, "3" : testCase3, "4" : testCase4, "5" : testCase5, "6" : testCase6, "7" : testCase7}
	
def runAllTests():#RUN ALL TESTS
	print("-------------------------------------------------------")
	print("[ ]  ID   STATUS   DESCRIPTION")
	print("-------------------------------------------------------")
	startTime = time.time()
	for i in sorted(testsDict):
		testsDict[i]()
	print("-------------------------------------------------------")
	stopTime = time.time()
	totalTime = int(stopTime - startTime)
	print("TESTING COMPLETE (total time = " + str(totalTime) + "s)\n")
	print("Total PASSED = " + str(passed) + "\nTotal FAILED = " + str(failed) + "\nTotal ERRORS = " + str(errors))
	print("-------------------------------------------------------")
	print("")

runAllTests()
driver.quit()


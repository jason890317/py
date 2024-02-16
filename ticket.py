from selenium import webdriver
import time
browser = webdriver.Chrome("./chromedriver")

#option.add_experimental_option("excludeSwitches", ['enable-automation']);
#option.add_argument("--headless") Use this and the following option to run Headless
#option.add_argument("disable-gpu")
#browser = webdriver.Chrome(executable_path='/home/srujan/chromedriver', options=option)

browser.get("https://forms.gle/FoAoauz53Xy7A4n68")

# # Use the following snippets to get elements by their class names
time.sleep(2)

textboxes = browser.find_elements_by_class_name("whsOnd")

# radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
# checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
submitbutton = browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")

# # Use the following snippets to get elements by their XPath
# otherboxes = browser.find_element_by_xpath("<Paste the XPath here>")

textboxes[0].send_keys("Hello World")

# radiobuttons[2].click()

# checkboxes[1].click()
# checkboxes[3].click()
print("sdfsdfsd")
submitbutton[0].click()

browser.quit()
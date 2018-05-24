from selenium import webdriver
import sys
import unittest
url = "https://www.facebook.com/"
test_id = "1"
test_scenario = "Verify the Login Section"
test_cases = "Enter valid UserId and password"
step_1 = "Go to page " + url
step_2 = "Enter valid UserId"
step_3 = "Enter vaild Password"
step_4 = "Click login"
expected_result = "Login successful"
login = sys.argv[1]
password = sys.argv[2]

print(test_scenario)
print(test_cases)
driver = webdriver.Firefox()
print(sys.argv)

print(step_1)
driver.get(url)

print(step_2)
login_input = driver.find_element_by_id("email")
login_input.clear()
login_input.send_keys(login)

print(step_3)
password_input = driver.find_element_by_id("pass")
password_input.clear()
password_input.send_keys(password)

print(step_4)
submit_button = driver.find_element_by_id("loginbutton")
submit_button.click()

assert "No results found." not in driver.page_source


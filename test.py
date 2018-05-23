from selenium import webdriver

url = "https://www.facebook.com/"
test_id = "1"
test_scenario = "Verify the Login Section"
test_cases = "Enter valid UserId and password"
step_1 = "Go to page" + url
step_2 = "Enter valid UserId"
step_3 = "Enter vaild Password"
step_4 = "Click login"
expected_result = "Login successful"

print(test_scenario)
print(test_cases)
driver = webdriver.Firefox()

print(step_1)
driver.get(url)

print(step_2)

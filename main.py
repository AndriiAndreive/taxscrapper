from selenium import webdriver
# Configure Chrome options for headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
# Initialize Chrome driver
driver = webdriver.Chrome(options=chrome_options)
# Navigate to the webpage you want to take a screenshot of
driver.get('https://www.example.com')
# Take a screenshot and save it to a file
driver.save_screenshot('screenshot.png')
# Close the browser
driver.quit()

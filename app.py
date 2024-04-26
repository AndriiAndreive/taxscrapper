from selenium import webdriver
import base64

# Configure Chrome options for headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration

# Initialize Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage you want to take a screenshot of
driver.get('https://www.example.com')

# Take a screenshot as a binary data
screenshot_binary = driver.get_screenshot_as_png()

# Encode the binary data to Base64
screenshot_base64 = base64.b64encode(screenshot_binary).decode('utf-8')

# Print the Base64 encoded string (or do whatever you need with it)
print(screenshot_base64)

# Close the browser
driver.quit()

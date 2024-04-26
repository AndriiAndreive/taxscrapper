import asyncio
from pyppeteer import launch

async def take_element_screenshot(url, element_selector, save_path):
    # Launch headless Chrome
    browser = await launch(executablePath='./chrome-win/chrome.exe', headless=True)
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})

    # Navigate to the URL
    await page.goto(url)

    # Wait for the element to be available
    await page.waitForSelector(element_selector)

    # Get the element's bounding box
    element_box = await page.querySelectorEval(element_selector, 'el => el.getBoundingClientRect()')

    # Take a screenshot of the element
    await page.screenshot({'path': save_path, 'clip': element_box})

    # Close the browser
    await browser.close()

# URL of the webpage
url = 'https://sandbox.oxylabs.io/products'

# Selector for the element to capture (replace 'element_selector' with the actual selector)
element_selector = '.egbpcqk0'

# Path to save the screenshot
save_path = 'element_screenshot.png'

# Run the async function to take the element screenshot
asyncio.get_event_loop().run_until_complete(take_element_screenshot(url, element_selector, save_path))

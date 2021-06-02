import pyautogui
from selenium import webdriver

chrome_driver_path = "/Users/nathanj/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://elgoog.im/t-rex/")

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

while True:
    pyautogui.keyDown("up")
    try:
        if pyautogui.locateOnScreen("tall_cacti.png") < 350:
            pyautogui.keyUp("up")
            pyautogui.keyDown("up")
        if pyautogui.locateOnScreen("two_cacti.png") < 350:
            pyautogui.keyUp("up")
            pyautogui.keyDown("up")
        if pyautogui.locateOnScreen("three_cacti.png") < 340:
            pyautogui.keyUp("up")
            pyautogui.keyDown("up")
    except TypeError:
        pass
    pyautogui.keyUp("up")

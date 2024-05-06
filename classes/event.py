import pyautogui


class Event:
    last = ""

    def __init__(self):
        pass

    def detect_image(self):
        element_detected = pyautogui.locateOnScreen(self)
        return element_detected, element_detected.x, element_detected.y

    @staticmethod
    def click_on():
        pyautogui.click() 
    
    @staticmethod
    def click_to(x, y):
        pyautogui.click(x, y)
    
    def set_last(self, value):
        self.last = value


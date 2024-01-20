import pyautogui


class element :
    last = ""

    def __init__(self):
        pass

    def detect(image_path):
        element_detected = pyautogui.locateOnScreen(image_path)        
        return element_detected,element_detected.x,element_detected.y

    def click_on(image_path):
        pyautogui.click() 
    
    def click_to(image_path,x,y):
        pyautogui.click(x,y) 
    
    def set_last(cls,value):
        cls.last = value

    def test():
        return "ok"
   



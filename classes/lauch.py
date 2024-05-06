import subprocess
import time
from classes.recognize import Recognize

i = 0
login_screen = 'resource.images.login_screen'
recognize = Recognize()

while i < 30:
    if not recognize.detect_image(login_screen,0.9):
        time.sleep(1)
    i = i + 1


subprocess.run(["python", "app.py"])
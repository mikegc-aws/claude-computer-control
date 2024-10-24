import pyautogui
from PIL import Image
import io
import base64
import time

class Computer:
    def __init__(self):
        self.display_width_px, self.display_height_px = pyautogui.size()
        pyautogui.FAILSAFE = False

    def key(self, key):
        pyautogui.press(key)
        time.sleep(0.1)

    def type(self, text):
        pyautogui.write(text)
        time.sleep(0.1)

    def mouse_move(self, x, y):
        pyautogui.moveTo(x, y)
        time.sleep(0.1)

    def left_click(self):
        pyautogui.click()
        time.sleep(0.1)

    def left_click_drag(self, start_x, start_y, end_x, end_y, duration=0.5):
        pyautogui.mouseDown(start_x, start_y)
        pyautogui.moveTo(end_x, end_y, duration=duration)
        pyautogui.mouseUp()
        time.sleep(0.1)

    def right_click(self):
        pyautogui.rightClick()
        time.sleep(0.1)

    def middle_click(self):
        pyautogui.middleClick()
        time.sleep(0.1)

    def double_click(self):
        pyautogui.click()
        time.sleep(1)
        pyautogui.doubleClick()
        time.sleep(1)
        pyautogui.doubleClick()
        time.sleep(0.1)

    def screenshot(self):
        screenshot = pyautogui.screenshot()
        buffered = io.BytesIO()
        screenshot.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()

    def cursor_position(self):
        x, y = pyautogui.position()
        return {"x": x, "y": y}


if __name__ == "__main__":
    computer = Computer()

    print(f"Size: {computer.display_width_px}x{computer.display_height_px}")

    # Save a screenshot to the local file system
    screenshot = computer.screenshot()
    # Decode the base64 string to bytes
    image_data = base64.b64decode(screenshot)
    # Create a PIL Image object from the bytes
    image = Image.open(io.BytesIO(image_data))
    # Save the image to the local file system
    image.save("screenshot.png")
    print("Screenshot saved as 'screenshot.png'")

    # Move the mouse to position 734, 90
    computer.mouse_move(734, 90)
    print("Mouse moved to position (734, 90)")

    # Perform a double click at the current mouse position
    computer.double_click()
    print("Double click performed at the current mouse position")

    # Perform a right click at the current mouse position
    computer.right_click()
    print("Right click performed at the current mouse position")

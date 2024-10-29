import pyautogui
import time

def capture_app_screenshot(app_region=None, output_file='screenshot.png'):
    """
    Capture a screenshot using pyautogui.
    
    Args:
        app_region (tuple): Optional (left, top, width, height) of screen region to capture
        output_file (str): Path where to save the screenshot
    
    Returns:
        The screenshot image object
    """
    # Give user time to switch to the desired window
    print("You have 3 seconds to switch to the window you want to capture...")
    time.sleep(3)
    
    # Take the screenshot
    if app_region:
        screenshot = pyautogui.screenshot(region=app_region)
    else:
        screenshot = pyautogui.screenshot()
    
    # Save the screenshot
    screenshot.save(output_file)
    print(f"Screenshot saved as {output_file}")
    
    return screenshot

# Example usage
if __name__ == "__main__":
    # Option 1: Capture full screen
    capture_app_screenshot(output_file='full_screen.png')
    
    # Option 2: Capture specific region
    # Example region: left=100, top=200, width=800, height=600
    capture_app_screenshot(app_region=(100, 200, 800, 600), output_file='region.png')
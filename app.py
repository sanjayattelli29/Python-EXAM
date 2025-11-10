import pyautogui
import time

# ====== Step 1: Read the content from your .txt file ======
file_path = 'code_to_type.txt'  # change this to your filename

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# ====== Step 2: Wait for 5 seconds so you can move your cursor ======
print("You have 5 seconds to place the cursor where you want the text to be typed...")
time.sleep(10)it

# ====== Step 3: Start typing the content exactly as it is ======
pyautogui.write(content, interval=0.01)  # interval controls typing speed (seconds per character)

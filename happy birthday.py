import pyfiglet
import random
import time
import os

def clear_screen():
    # Clears the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def happy_birthday():
    colors = ['31', '32', '33', '34', '35', '36', '37']  # ANSI color codes
    message = pyfiglet.figlet_format("Happy Birthday!", font="slant")
    
    try:
        while True:
            clear_screen()
            color = random.choice(colors)
            print(f"\033[{color}m{message}\033[0m")
            time.sleep(0.5)
    except KeyboardInterrupt:
        clear_screen()
        print("🎉 Birthday celebration ended. Have a great day! 🎉")

happy_birthday()

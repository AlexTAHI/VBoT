from engine import * # bot class importing
import keyboard

# bot loading
bot = Engine()

# detection
print("[INFO] Starting detection..")
while keyboard.is_pressed('q') == False:
    bot.game()
print("[INFO] Bot shutdown..")
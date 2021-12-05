from engine import * # bot class importing
import keyboard

# bot loading
bot = Engine()

# detection
print("[INFO] Starting detection..")
while bot.isVoteTerminated == False or keyboard.is_pressed('q') == False:
    bot.vote()
print("[INFO] Bot shutdown..")
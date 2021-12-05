# piano tiles bot
import pyautogui
import time
import random
import win32api, win32con
import os

# clean the terminal
os.system('cls')

# discomment this line to show mouse position
#pyautogui.displayMousePosition()

class Engine:
    # TODO: Constructor ////
    def __init__(self):
        # TODO: Properties ////
        print("[INFO] Bot loading..")
        self.link = "https://www.wecanda.com/entrepreneur-social/"
        self.isCaptchaValidate = False
        self.isVoteTerminated = False
        self.checkCandidat = False
        # buttons images
        self.radio_candidat = pyautogui.locateOnScreen("./dataset/radio_candidat.jpg", confidence = 0.8)
        self.captcha = pyautogui.locateOnScreen("./dataset/captcha.png", confidence = 0.8)
        self.validate_captcha = pyautogui.locateOnScreen("./dataset/validate_captcha.png", confidence = 0.8)
        self.vote_btn = pyautogui.locateOnScreen("./dataset/vote_btn.png", confidence = 0.8)
    # TODO: Method ////
    # Method to click on the screen
    def click(self, position: tuple):
        """
        This method is used to press mouse on a specific point of screen
        Only one parameter is the position to click
        """
        win32api.SetCursorPos(position) # move the cursor to the new position
        time.sleep(0.5)
        # call event to click on the screen
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01) # pause the script every 10ms to click correctly
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0) # call event to release previous click
    # Method to begin the vote
    def vote(self):
        self.reload()
        if not self.isVoteTerminated:
            # detect candidat radio button and click it
            if self.isBtnOnScreen(self.radio_candidat):
                self.checkCandidat = True
                self.click(self.centerBtnCoords)
                print("[INFO] Radio Button clicked !")
            # detect captcha verification and valid it
            if self.isBtnOnScreen(self.captcha)and self.checkCandidat:
                self.click(self.centerBtnCoords)
                # try to validate the Captcha validation test
                while not self.isBtnOnScreen(self.validate_captcha):
                    print("[INFO] Captcha validation success !")
                    time.sleep(1)
                    if self.isBtnOnScreen(self.vote_btn):
                        self.click(self.centerBtnCoords)
                        print("[INFO] Vote Button clicked !")
                        self.isCaptchaValidate = True
                        self.isVoteTerminated = True
                        break
                    """
                    if self.isBtnOnScreen(self.validate_captcha):
                        print("[INFO] Captcha validation success !")
                        if self.isBtnOnScreen(self.vote_btn):
                            self.click(self.centerBtnCoords)
                            print("[INFO] Vote Button clicked !")
                            self.isCaptchaValidate = True
                            self.isVoteTerminated = True
                            break
                    else:
                        print("[ERROR] Can't validate the Captcha Test")
                        self.isCaptchaValidate = False
                    """
            if self.isBtnOnScreen(self.vote_btn) and self.isCaptchaValidate:
                self.isVoteTerminated = True
                self.click(self.centerBtnCoords)
                print("[INFO] Vote Button clicked !")
                print("[SUCCESS] Vote terminated with success !")
            else:
                print("[ERROR] Captcha validation failed ")
                self.isVoteTerminated = True
            # Shutdown the bot when the vote is over
            if self.isVoteTerminated:
                print("[END] Bot logout...")
    # Method to know if any button is on screen
    def isBtnOnScreen(self, btn):
        if btn != None:
            self.centerBtnCoords = [int(btn[0] + (btn[2] / 2)), int(btn[1] + (btn[3] / 2))]
            return True
        else: return False
    # Reload method
    def reload(self):
        self.radio_candidat = pyautogui.locateOnScreen("./dataset/radio_candidat.jpg", confidence = 0.8)
        self.captcha = pyautogui.locateOnScreen("./dataset/captcha.png", confidence = 0.8)
        self.vote_btn = pyautogui.locateOnScreen("./dataset/vote_btn.png", confidence = 0.8)
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
        self.previousTile = 'start'
        self.centerBtnCoords = []
        self.hasGameStart = False
        self.gameLink = "https://www.jeuxjeuxjeux.fr/jeu/piano-tiles-2.html"
        # buttons images
        self.startBtn = pyautogui.locateOnScreen("PianoTilesBot/img/startBtn.png", confidence = 0.8 )
        self.restartBtn = pyautogui.locateOnScreen("PianoTilesBot/img/restartBtn.png", confidence = 0.8 )
        self.skipBtn = pyautogui.locateOnScreen("PianoTilesBot/img/skipBtn.png", confidence = 0.8 )
        self.nothanksBtn = pyautogui.locateOnScreen("PianoTilesBot/img/nothanksBtn.png", confidence = 0.8 )
        self.playBtn = pyautogui.locateOnScreen("PianoTilesBot/img/playBtn.png", confidence = 0.8 )
        self.nextBtn = pyautogui.locateOnScreen("PianoTilesBot/img/nextBtn.png", confidence = 0.8 )
        # tiles positions
        self.columns = {
            'Column1' : (360, 340),
            'Column2' : (410, 340),
            'Column3' : (460, 340),
            'Column4' : (510, 340),
        }
    # TODO: Method ////
    # Method to click on the screen
    def click(self, position: tuple):
        """
        This method is used to press mouse on a specific point of screen
        Only one parameter is the position to click
        """
        win32api.SetCursorPos(position) # move the cursor to the new position
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0) # call event to click on the screen
        time.sleep(0.01) # pause the script every 10ms to click correctly
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0) # call event to release previous click
    # Method to detect all tiles
    def detect(self):
        """
        This method is used to detect all tiles in a specific position
        when the pixel attached to a colmun become black, this method
        call the Click method.
        No parameter required.
        """
        # check if the Red value equals to black
        # We don't need to check all colors value, red is enough
        for (name, column) in self.columns.items():
            if pyautogui.pixel(column[0], column[1])[0] <= 5 and self.previousTile != name:
                self.click(column)
                self.previousTile = name
                print(f"[DONE] {name} clicked !")
    # Method to begin the game
    def game(self):
        self.reload()
        if not self.hasGameStart:
            # play button
            if self.isBtnOnScreen(self.playBtn):
                self.click(self.centerBtnCoords)
                print("[INFO] Button Play clicked !")
            # start button
            if self.isBtnOnScreen(self.startBtn):
                self.click(self.centerBtnCoords)
                self.hasGameStart = True
                print("[INFO] Button Start clicked !")
            # skip button
            if self.isBtnOnScreen(self.skipBtn):
                self.click(self.centerBtnCoords)
                print("[INFO] Button Skip clicked !")
            # nothanks button
            if self.isBtnOnScreen(self.nothanksBtn):
                self.click(self.centerBtnCoords)
                print("[INFO] Button Nothanks clicked !")
        # restart button
        if self.isBtnOnScreen(self.restartBtn):
            self.click(self.centerBtnCoords)
            self.hasGameStart = True
            print("[INFO] Button Restart clicked !")
        else:
            self.hasGameStart = False
        # call method to detect all tiles
        self.detectTile()
    # Method to know if any button is on screen
    def isBtnOnScreen(self, btn):
        if btn != None:
            self.centerBtnCoords = [int(btn[0] + (btn[2] / 2)), int(btn[1] + (btn[3] / 2))]
            return True
        else: return False
    # Reload method
    def reload(self):
        self.startBtn = pyautogui.locateOnScreen("PianoTilesBot/img/startBtn.png", confidence = 0.8 )
        self.restartBtn = pyautogui.locateOnScreen("PianoTilesBot/img/restartBtn.png", confidence = 0.8 )
        self.skipBtn = pyautogui.locateOnScreen("PianoTilesBot/img/skipBtn.png", confidence = 0.8 )
        self.nothanksBtn = pyautogui.locateOnScreen("PianoTilesBot/img/nothanksBtn.png", confidence = 0.8 )
        self.playBtn = pyautogui.locateOnScreen("PianoTilesBot/img/playBtn.png", confidence = 0.8 )
        self.nextBtn = pyautogui.locateOnScreen("PianoTilesBot/img/nextBtn.png", confidence = 0.8 )
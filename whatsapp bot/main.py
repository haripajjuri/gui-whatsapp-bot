import pyautogui as pt
import pyperclip
from time import sleep
import random

sleep(5)

def copy_msg():
    a,b = pt.locateCenterOnScreen(r'''\whatsapp bot\smiley.jpg''',confidence=.7)
    try:
        pt.moveTo(a,b,duration=.2)
        pt.moveRel(50,-115,duration=.2)
        pt.tripleClick()
        pt.rightClick()
        pt.moveRel(30,-220,duration=.2)
        pt.click()
        print(pyperclip.paste())
    except:
        print("not found")


#open and ignore muted messages
muted=1
def open_muted_msgs():
    global muted
    try:
        x,y = pt.locateCenterOnScreen("\whatsapp bot\muted.jpg",confidence=.95)
        pt.moveTo(x-160,y,duration=.2)
        pt.click()
    except:
        muted = 0


#open the unread messages
unread=1
def open_unread_msgs():
    global unread
    try:
        x,y = pt.locateCenterOnScreen(r'''\whatsapp bot\unread.jpg''',confidence=.75)
        pt.moveTo(x-160,y,duration=.2)
        pt.click()
        copy_msg()#copy the message

    except:
        unread=0


def check_messages():
    while(muted==1):#ignore all the muted messages
        open_muted_msgs()

    while(unread==1):#opens all the unread msgs and copy them
        open_unread_msgs()
        
    
check_messages()



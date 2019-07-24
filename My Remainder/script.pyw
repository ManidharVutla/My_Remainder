import pyttsx
from win32com.client import *

import os


engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Welcome Manidhar Vutla')

with open('/My_Remainder.txt') as line:
   for lines in line:
       if (lines==  '\n' or """Save Before Closing	Don't break lines ! Write Continously"""):
          pass
       else:
           lines=line

engine.say(lines)
os.startfile('/My_Remainder.txt')

engine.runAndWait()

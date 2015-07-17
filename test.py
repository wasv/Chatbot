#!/usr/bin/env python
import aiml
#import pyttsx
import os, marshal
try:
  import pyreadline as readline
except ImportError:
  import readline
import sys

if (sys.platform != 'win32' or 'ANSICON' in os.environ):
  class bcolors:
      BOT = '\033[36m'
      USER = '\033[32m'
      ERROR = '\033[31m'
      ENDC = '\033[0m'
else:
  class bcolors:
    BOT = ''
    USER = ''
    ERROR = ''
    ENDC = ''
  
  
speak = True
#if len(sys.argv) > 1:
  # print "Quiet Mode"
  # speak = False
  
specials = ["reload", "exit", "quit"]
# if speak: engine = pyttsx.init()
# if speak: engine.setProperty('rate', 130)


k = aiml.Kernel()
def learn():
  k.learn("my-bot.aiml")
  k.learn("aiml/*.aiml")
  k.saveBrain(".jarvis.brn")
  user = k.setPredicate("user", "USER")
  
def close():
  print
  k.saveBrain(".jarvis.brn")

  user = k.getSessionData()
  sf = file(".jarvis.ses", "wb")
  marshal.dump(user, sf)
  sf.close()
        
  response = bcolors.BOT + "Goodbye "+user['_global']['user'] + bcolors.ENDC
        
  print bot+": "+response
  # if speak: engine.endLoop()
  # if speak: engine.say(response)
  # if speak: engine.runAndWait()
  sys.exit()
  
k = aiml.Kernel()
k.setBotPredicate("name", "JARVIS")
bot = k.getBotPredicate("name")
if os.path.isfile(".jarvis.brn"): #Load saved brain
  k.bootstrap(brainFile = ".jarvis.brn")
  
  if os.path.isfile(".jarvis.ses"): #Load saved session
    sessionFile = file(".jarvis.ses", "rb")
    session = marshal.load(sessionFile)
    sessionFile.close()
    for pred,value in session['_global'].items():
      k.setPredicate(pred, value)
    user = k.getPredicate("user")
    
    print bcolors.BOT + bot+": "+ k.respond("welcome") + bcolors.ENDC
else: #First time setup
  learn()
  
  
#if speak: engine.startLoop(False)

while True: 
  try: 
    user = k.getPredicate("user")
    request = raw_input(bcolors.USER +user+": "+ bcolors.ENDC)
    if request in specials:
      if request == "reload":
        learn()
        response = k.respond("reload")
      if request == "exit" or request == "quit":
        close()
    else:
      response = k.respond(request)
      
    if response == "": response = bcolors.ERROR+"I didn't understand that. Could you try again?"+bcolors.ENDC
    
    print bcolors.BOT + bot+": "+response + bcolors.ENDC
    # if speak: engine.say(response)
    # if speak: engine.iterate()
  except EOFError:
    close()
  except KeyboardInterrupt:
    close()


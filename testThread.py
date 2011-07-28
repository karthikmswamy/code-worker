import os
from KThread import *

def func():
  print 'Function started'
  os.system('java -jar ' + 'TournamentServer-GUI/gui/test/lib/jstestdriver/JsTestDriver.jar --port 9876')
  print 'Function finished'

A = KThread(target=func)
A.start()
A.kill()

print 'End of main program'

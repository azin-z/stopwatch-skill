from mycroft import MycroftSkill, intent_file_handler
import time
from time import sleep
from threading import Thread

class Stopwatch(MycroftSkill):
    def __init__(self):
        self.starttime = None 
        MycroftSkill.__init__(self)
    
    def printStopwatchUpdate(self):
        while self.starttime is not None:
            sleep(60)
            self.speak('stopwatch running for {} minutes'.format(round((time.time()-self.starttime)/60)))

    @intent_file_handler('stopwatch.intent')
    def handle_stopwatch(self, message):
        self.starttime = time.time()
        self.speak_dialog('stopwatch')
        Thread(target=self.printStopwatchUpdate).start()

    @intent_file_handler('stopstopwatch.intent')
    def handle_stopwatch_stop(self, message):
        if self.starttime is None:
            self.speak("No stopwatch running, please start one first")
            return
        self.log.info("stopping stopwatch")
        self.speak('Stopwatch recorded {} seconds'.format(round(time.time()-self.starttime)))
        self.starttime = None

def create_skill():
    return Stopwatch()
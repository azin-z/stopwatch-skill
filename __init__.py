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
            self.speak('stopwatch has been running for {} seconds'.format(time.time()-self.starttime))
            sleep(5)


    @intent_file_handler('stopwatch.intent')
    def handle_stopwatch(self, message):
        self.starttime = time.time()
        self.speak_dialog('stopwatch')
        Thread(target=printStopwatchUpdate).start()

    @intent_file_handler('stopstopwatch.intent')
    def handle_stopwatch_stop(self, message):
        if self.starttime is None:
            self.speak("No stopwatch running, please start one first")
            return
        self.log.info("stopping stopwatch")
        self.speak('Stopwatch recorded {} seconds'.format(time.time()-self.starttime))
        self.starttime = None

def create_skill():
    return Stopwatch()
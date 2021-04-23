from mycroft import MycroftSkill, intent_file_handler
import time
from threading import Timer

class Stopwatch(MycroftSkill):
    def __init__(self):
        self.starttime = None 
        MycroftSkill.__init__(self)
    
    def printStopwatchUpdate(self, currentTime):
        if self.starttime is not None:
            self.speak('stopwatch has been running for {} seconds'.format(currentTime-self.starttime))
            Timer(5.0, self.printStopwatchUpdate, (time.time())).start()


    @intent_file_handler('stopwatch.intent')
    def handle_stopwatch(self, message):
        self.starttime = time.time()
        self.speak_dialog('stopwatch')
        self.printStopwatchUpdate(time.time())

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
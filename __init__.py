from mycroft import MycroftSkill, intent_file_handler
import time
from threading import Timer

class Stopwatch(MycroftSkill):
    def __init__(self):
        self.starttime = None 
        MycroftSkill.__init__(self)
    
    def printStopwatchUpdate(self, currentTime):
        self.speak('stopwatch has been running for {} seconds'.format(currentTime-self.starttime))

    @intent_file_handler('stopwatch.intent')
    def handle_stopwatch(self, message):
        self.starttime = time.time()
        self.speak_dialog('stopwatch')
        Timer(1.0, self.printStopwatchUpdate, (time.time()))

    @intent_file_handler('stopstopwatch.intent')
    def handle_stopwatch_stop(self, message):
        self.log.info("stopping stopwatch")
        duration = time.time() - self.starttime
        self.log.info(duration)
        self.speak("stopwatch duration is {}".format(round(duration)))

def create_skill():
    return Stopwatch()
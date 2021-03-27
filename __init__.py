from mycroft import MycroftSkill, intent_file_handler
import time

class Stopwatch(MycroftSkill):
    def __init__(self):
        self.starttime = None 
        MycroftSkill.__init__(self)

    @intent_file_handler('stopwatch.intent')
    def handle_stopwatch(self, message):
        self.starttime = time.time()
        self.log.info(message)
        self.log.info("got a hang of logging")

        self.speak_dialog('stopwatch')

    @intent_file_handler('stopstopwatch.intent')
    def handle_stopwatch_stop(self, message):
        self.log.info("stopping stopwatch")
        duration = time.time() - self.starttime
        self.log.info(duration)
        self.speak("stopwatch duration is {}".format(duration))

def create_skill():
    return Stopwatch()
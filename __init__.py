from mycroft import MycroftSkill, intent_file_handler
import time

class Stopwatch(MycroftSkill):
    def __init__(self):
        # self.started = False
        # self.startTime = None
        MycroftSkill.__init__(self)

    @intent_file_handler('stopwatch.intent')
    def handle_stopwatch(self, message):
        # self.startTime = time.time()
        self.log.info(message)
        self.log.info("got a hang of logging")
        self.speak_dialog('stopwatch')
    
    # @intent_file_handler('stopstopwatch.intent')
    # def handle_stopwatch(self, message):
    #     duration = time.time() - self.startTime
    #     self.log.info(message)
    #     self.log.info("got a hang of logging in stop")
    #     self.log.info(duration)
    #     self.speak('stopwatch is at {}'.format(duration))


def create_skill():
    return Stopwatch()


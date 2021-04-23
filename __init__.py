from mycroft import MycroftSkill, intent_file_handler
import time
import datetime
from time import sleep
from threading import Thread

def fix_plural(string, value):
    if value > 1:
        return string + "s "
    return string + " "

def get_elaspsed_time_string(elapsedTime):
    tdelta = datetime.timedelta(seconds=elapsedTime)
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)

    day = "{days} day" if d["days"]>0 else "" 
    hour = "{hours} hour" if d["hours"]>0 else "" 
    minutes = "{minutes} minute" if d["minutes"]>0 else ""
    seconds = "and {seconds} second" if d["seconds"]>0 else ""
    fmt = fix_plural(day, d["days"]) + fix_plural(hour, d["hours"]) + fix_plural(minutes, d["minutes"]) + fix_plural(seconds, d["minutes"])
    return fmt.format(**d)


class Stopwatch(MycroftSkill):
    def __init__(self):
        self.starttime = None 
        MycroftSkill.__init__(self)
    
    def printStopwatchUpdate(self):
        while self.starttime is not None:
            sleep(60)
            self.speak('stopwatch running for {}'.format(get_elaspsed_time_string(round(time.time()-self.starttime))))

    @intent_file_handler('stopwatch.intent')
    def handle_stopwatch(self, message):
        self.starttime = time.time()
        self.speak_dialog('stopwatch')
        Thread(target=self.printStopwatchUpdate).start()

    @intent_file_handler('stopwatchupdate.intent')
    def handle_stopwatch_update_request(self, message):
        self.speak_dialog('stopwatch')
        self.speak('Stopwatch has recorded {} seconds'.format(get_elaspsed_time_string(round(time.time()-self.starttime))))

    @intent_file_handler('stopstopwatch.intent')
    def handle_stopwatch_stop(self, message):
        if self.starttime is None:
            self.speak("No stopwatch running, please start one first")
            return
        self.log.info("stopping stopwatch")
        self.speak('Stopwatch recorded {} seconds'.format(get_elaspsed_time_string(round(time.time()-self.starttime))))
        self.starttime = None

def create_skill():
    return Stopwatch()


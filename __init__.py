from mycroft import MycroftSkill, intent_file_handler
import time
import datetime
from time import sleep
from threading import Thread

def fix_plural(string, value):
    if value > 1:
        return string + "s "
    return string + " "




class Stopwatch(MycroftSkill):
    def __init__(self):
        self.starttime = None 
        MycroftSkill.__init__(self)
    
    def get_elaspsed_time_string(self):
        elapsedTime = round(time.time() - self.starttime)
        tdelta = datetime.timedelta(seconds=elapsedTime)
        d = {"days": tdelta.days}
        d["hours"], rem = divmod(tdelta.seconds, 3600)
        d["minutes"], d["seconds"] = divmod(rem, 60)

        day = "{days} day" if d["days"]>0 else "" 
        hour = "{hours} hour" if d["hours"]>0 else "" 
        minutes = "{minutes} minute" if d["minutes"]>0 else ""
        seconds = "{seconds} second" if d["seconds"]>0 else ""
        if day+hour+minutes != "" and d["seconds"]>0:
            seconds = "and " + seconds
        fmt = fix_plural(day, d["days"]) + fix_plural(hour, d["hours"]) + fix_plural(minutes, d["minutes"]) + fix_plural(seconds, d["seconds"])
        return fmt.format(**d)

    def printStopwatchUpdate(self):
        while self.starttime is not None:
            sleep(60)
        self.speak_dialog('stopwatch_update', {'time': self.get_elaspsed_time_string()})

    def no_stopwatch_running_handler(self):
        if self.starttime is None:
            self.speak("No stopwatch running, please start one first")
            return True
        return False

    @intent_file_handler('stopwatch.intent')
    def handle_stopwatch(self, message):
        self.starttime = time.time()
        self.speak_dialog('stopwatch_start')
        Thread(target=self.printStopwatchUpdate).start()

    @intent_file_handler('stopwatchupdate.intent')
    def handle_stopwatch_update_request(self, message):
        if self.no_stopwatch_running_handler():
            return
        self.speak_dialog('stopwatch_update', {'time': self.get_elaspsed_time_string()})
        self.starttime = None

    @intent_file_handler('stopstopwatch.intent')
    def handle_stopwatch_stop(self, message):
        if self.no_stopwatch_running_handler():
            return
        self.speak_dialog('stopwatch_stop', {'time': self.get_elaspsed_time_string()})
        self.starttime = None

def create_skill():
    return Stopwatch()


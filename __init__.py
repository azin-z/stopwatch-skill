from mycroft import MycroftSkill, intent_file_handler


class Stopwatch(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('stopwatch.intent')
    def handle_stopwatch(self, message):
        self.log.info(message)
        self.log.info("got a hang of logging")

        self.speak_dialog('stopwatch')


def create_skill():
    return Stopwatch()


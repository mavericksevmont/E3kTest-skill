from mycroft import MycroftSkill, intent_file_handler


class Nite(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('nite.intent')
    def handle_bark(self, message):
        self.speak_dialog('nite')


def create_skill():
    return Nite()


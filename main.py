# IMPORTS LIBS
from bot.bot.Bot import Bot
from bot.bot.handler import MessageHandler
from datetime import datetime
import random
import numpy as np



class Main:
    def __init__(self):
        self.TOKEN = "PUT THERE YOUR TOKEN FORM METABOT"
        self.bot = Bot(token=self.TOKEN)
        self.chat_nick = "CHAT LINK"
        self.chatId = "TAKE CHAT IF FROM EVENT AND PUT THERE"
        self.WeekTable = {
            'Monday': ['Ekologiya amaly \t316', 'Diskret matematika leksiya \tMejlisler zaly',
                       'Kodirleme nazaryeti \t342',
                       'Diskret matematika amaly \t342', 'Ahtimalyklar nazaryeti leksiya \t436'],
            'Tuesday': ['Bedenterbiye \tsport zal', 'OGP amaly \t216', 'Ulgamlayyn programmirleme amaly \t408',
                        'Ulgamlayyn programmirleme leksiya \t418'],
            'Wednesday': ['Ekologiya leksiya \t412', 'Yokary Matematika leksiya \t436', 'Filosofiya leksiya \t436'],
            'Thursday': ['Howandarlyk \t318', 'OGP leksiya \t436', 'Howandarlyk \t318', 'OGP leksiya \t436',
                         'Kompyuter torlary \t436', 'Ulgamlayyn programmirleme leksiya \t436'],
            'Friday': ['Inlis dili \t410', 'Kompyuter torlary amaly \t410', 'Filosofiya amaly \t410', '',
                       'Inlis dili \t410'],
            'Saturday': ['Ahtimalyk nazaryeti amaly \t208', 'Kodirlemegin nazaryeti leksiya \t418',
                         'Yokary matematika amaly \t310']
        }

        # ADD SOME BAD WORDS 
        self.BadWords = []

        # SOME WORDS WHEN SOMEBODY SEND A BAD WORDS 
        self.words = []
        self.process = []
        self.temp = []
        self.nums = list(range(1, 101))
        self.SomeWords = []
        self.Week = int(datetime.now().date().strftime('%W'))

    # MESSAGE FUNCTION WHEN SOMEBODY REQUEST 1 DAY SCHEDULE
    def message_cb(self, bot, event):
        ty = event.chat_type
        if ty == 'group' and event.from_chat == self.chatId:
            if event.text in ['SOME WORDS TO ACTVIE THE BOT']:
                bot.send_text(chat_id=self.chat_nick, text='PUT THERE YOUR TEXT WHEN SOMEBODY ASK BOT')

            if int(event.text) == 1:
                monday = self.WeekTable['Monday']
                if self.Week % 2 == 0:
                    bot.send_text(chat_id=self.chat_nick,
                                  text=f'Sen ucin {event.text} gun raspaisaniye {event.message_author["firstName"]}')
                    bot.send_text(chat_id=self.chat_nick, text=f'{monday[1]} \t\n{monday[3]} \t\n{monday[4]}')
                else:
                    bot.send_text(chat_id=self.chat_nick,
                                  text=f'Sen ucin {event.text} gun raspaisaniye {event.message_author["firstName"]}')
                    bot.send_text(chat_id=self.chat_nick, text=f'{monday[0]} \t\n{monday[2]} \t\n{monday[4]}')

            elif int(event.text) == 2:
                tuesday = self.WeekTable['Tuesday']
                if self.Week % 2 == 0:
                    bot.send_text(chat_id=self.chat_nick,
                                  text=f'Sen ucin {event.text} gun raspaisaniye {event.message_author["firstName"]}')
                    bot.send_text(chat_id=self.chat_nick, text=f'{tuesday[0]} \t\n{tuesday[1]} \t\n{tuesday[3]}')
                else:
                    bot.send_text(chat_id=self.chat_nick, text=f'{tuesday[0]} \t\n{tuesday[1]} \t\n{tuesday[2]}')

            elif int(event.text) == 3:
                bot.send_text(chat_id=self.chat_nick,
                              text=f'Sen ucin {event.text} gun raspaisaniye {event.message_author["firstName"]}')
                wednesday = self.WeekTable['Wednesday']
                bot.send_text(chat_id=self.chat_nick, text=f'{wednesday[0]} \t\n{wednesday[1]} \t\n{wednesday[2]}')

            elif int(event.text) == 4:
                thursday = self.WeekTable['Thursday']
                if self.Week % 2 == 0:
                    bot.send_text(chat_id=self.chat_nick,
                                  text=f'Sen ucin {event.text} gun raspaisaniye {event.message_author["firstName"]}')
                    bot.send_text(chat_id=self.chat_nick, text=f'{thursday[1]} \t\n{thursday[3]} \t\n{thursday[5]}')
                else:
                    bot.send_text(chat_id=self.chat_nick,
                                  text=f'Sen ucin {event.text} gun raspaisaniye {event.message_author["firstName"]}')
                    bot.send_text(chat_id=self.chat_nick, text=f'{thursday[0]} \t\n{thursday[2]} \t\n{thursday[4]}')

            elif int(event.text) == 5:
                friday = self.WeekTable['Friday']
                if self.Week % 2 == 0:
                    bot.send_text(chat_id=self.chat_nick,
                                  text=f'Sen ucin {event.text} gun raspaisaniye {event.message_author["firstName"]}')
                    bot.send_text(chat_id=self.chat_nick, text=f'{friday[1]} \t\n{friday[2]}\t\n{friday[4]}')
                else:
                    bot.send_text(chat_id=self.chat_nick,
                                  text=f'Sen ucin {event.text} gun raspaisaniye {event.message_author["firstName"]}')
                    bot.send_text(chat_id=self.chat_nick, text=f'{friday[0]} \t\n{friday[2]} \t\n Domoy 2 para ')

            elif int(event.text) == 6:
                saturday = self.WeekTable['Saturday']
                bot.send_text(chat_id=self.chat_nick, text=f'Sen ucin {event.text} gun raspaisaniye {event.message_author["firstName"]}')
                bot.send_text(chat_id=self.chat_nick, text=f'{saturday[0]} \t\n{saturday[1]} \t\n{saturday[2]}')

            elif int(event.text) > 6:
                bot.send_text(chat_id=self.chat_nick, text=f'Kellan yerindemi senin wasyek {event.message_author["firstName"]}')

            else:
                pass
        else:
            pass

    # FUNCTION WHEN BOT STARTED
    def SayHi(self):
        self.bot.send_text(chat_id=self.chat_nick, text='HELLO WORLD')

    # SWEAR WORDS FUNCTION WHEN SOME BODY TYPED
    def badWord(self, bot, event):
        # FILTERING WORDS FOR SWEAR WORDS
        if event.chat_type == 'group' and event.from_chat == self.chatId:
            text = event.text.split()
            print(event)
            self.process.append(text)
            for i in self.process:
                for j in i:
                    if j in self.BadWords:
                        self.process.clear()
                        bot.send_text(chat_id=self.chat_nick, text=f'{random.choice(self.words)} {event.message_author["firstName"]}')
                        bot.delete_messages(chat_id=self.chat_nick, msg_id=event.msgId)
        else:
            pass
    

    # SMART BOT FUNCTION CHATING WITH CHAT MEMBERS
    def CleverBot(self, bot, event):
        if event.chat_type == 'group' and event.from_chat == self.chatId:
            text = event.text
            self.SomeWords.append(text)

            for i in self.SomeWords:
                for j in i:
                    if j in self.BadWords:
                        self.SomeWords.remove(j)
                    else:
                        pass

            for k in str(self.nums):
                if k in self.SomeWords:
                    self.SomeWords.remove(k)
                else:
                    pass
            
            # avoid duplicate words
            self.SomeWords[:] = np.unique(self.SomeWords)

            if len(self.SomeWords) > 50:
                if event.text not in str(self.nums):
                    bot.send_text(chat_id=self.chat_nick, text=random.choice(self.SomeWords))
                else:
                    pass
            else:
                pass
        else:
            pass


    # GLOBAL FUNCTION TO START ALL FUNCTIONS
    def start(self):
        self.bot.dispatcher.add_handler(MessageHandler(callback=self.badWord))
        self.bot.dispatcher.add_handler(MessageHandler(callback=self.CleverBot))
        self.bot.dispatcher.add_handler(MessageHandler(callback=self.message_cb))
        # KEEP BOT ACTIVE
        self.bot.start_polling()
        self.bot.idle()

# RUN 
if __name__ == '__main__':
    t = Main()
    t.SayHi()
    t.start()
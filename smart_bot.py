# IMPORTS LIBS
from bot.bot.Bot import Bot
from bot.bot.handler import MessageHandler
import random
import numpy as np


class Main:
    def __init__(self):
        self.TOKEN = ""
        self.bot = Bot(token=self.TOKEN)

        # ADD SOME BAD WORDS
        self.BadWords = ['type some swear words']

        # Some words if somebody says swear words
        self.words = ['Soyunme bratiska akylly bol', 'Name diyyan sen?? Akylly bol', 'Soyunmek bolanok',
                      'Bir birini sylammaly oglanlar', 'Bolly eday diyyan sana soyunme dos']

        self.process = []
        self.nums = list(range(1, 101))
        self.SomeWords = []

    def message_cb(self, bot, event):

        print(f"---------------------------\n"
              f"Name: {event.message_author['firstName']} "
              f"\nUserId: {event.message_author['userId']} "
              f"\nChatId: {event.from_chat}"
              f"\nText: {event.text} \nmsgId: {event.msgId} "
              f"\n---------------------------")

        if event.text in ['Bot', 'bot']:
            bot.send_text(chat_id=event.from_chat, text=f'Hi Mr. {event.message_author["firstName"]}'
                                                        f'\nЯ умный бот который с вами могу переписоваться.'
                                                        f' Но для этого мне нужно как минимум 50 слов для моего словарного запаса.')
        else:
            ...

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

        if len(self.SomeWords) > 20:
            if event.text not in str(self.nums):
                bot.send_text(chat_id=event.from_chat,
                              text=random.choice(self.SomeWords))
            else:
                pass
        else:
            pass

    # SWEAR WORDS FUNCTION WHEN SOME BODY TYPED
    def badWord(self, bot, event):
        # FILTERING WORDS FOR SWEAR WORDS
        text = event.text.split()
        self.process.append(text)
        for i in self.process:
            for j in i:
                if j in self.BadWords:
                    self.process.clear()
                    bot.send_text(
                        chat_id=event.from_chat, text=f'{random.choice(self.words)} {event.message_author["firstName"]}')
                    bot.delete_messages(
                        chat_id=event.from_chat, msg_id=event.msgId)

    # GLOBAL FUNCTION TO START ALL FUNCTIONS

    def start(self):
        self.bot.dispatcher.add_handler(MessageHandler(callback=self.badWord))
        self.bot.dispatcher.add_handler(
            MessageHandler(callback=self.message_cb))

        # KEEP BOT ACTIVE
        self.bot.start_polling()
        self.bot.idle()


# RUN
if __name__ == '__main__':
    t = Main()
    t.start()

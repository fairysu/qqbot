from qqbot import QQBotSlot as qqbotslot, RunBot

@qqbotslot
def onQQMessage(bot, contact, member, content):
    if content == 'hello':
        bot.SendTo(contact, 'HELLO')
    elif content == 'stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()

if __name__ == '__main__':
    RunBot()

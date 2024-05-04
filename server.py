from bot import telegram_chatbot
import subprocess
import time
import gizoogle

bot = telegram_chatbot("config.cfg")



def make_reply():
    p = subprocess.Popen("speedtest", shell=True, stdout=subprocess.PIPE)
    p.wait()
    #out, err = p.communicate()
    out = p.communicate()
    print(out)
    print("\nfinish_test")
    reply = str(out)
    return reply
    #time.sleep(10)
    '''reply = None
    if msg is not None:
        reply = out
    return reply
    time.sleep(1)'''

update_id = None

while True:
    for i in range(10):
        reply = make_reply()+'\n'+str(i)
        bot.send_message(reply, 949048300)
        print('msg_sent', str(i))
        print('this is count', str(i))
        time.sleep(60*5)
    '''
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
    '''

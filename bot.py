#Importamos bibliotecas
import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
#Declaramos Variables
blue = 19
yellow = 6 
red = 13 
green = 5
#Inicializamos los pines en nivel bajo
now = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(blue, GPIO.OUT)
GPIO.output(blue, 0)

GPIO.setup(yellow, GPIO.OUT)
GPIO.output(yellow,0)

GPIO.setup(red, GPIO.OUT)
GPIO.output(red, 0)

GPIO.setup(green, GPIO.OUT)
GPIO.output(green, 0)
#Definimos una funcion

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Received: %s' % command)
    message = "Comandos: "
    telegram_bot.sendMessage (chat_id, message)
    message = "all on \n all off \n sala on \n patio on \n cocina on \n comedor on \n sala off \n patio off \n cocina off \n comedor off \n"
    telegram_bot.sendMessage (chat_id, message)
    if 'on' in command:
        message = 'on' 
        if 'sala' in command:
            message = message + "sala"
            GPIO.output(blue, 1)
        if 'comedor' in command:
            message = message + "comedor"
            GPIO.output(yellow, 1)
        if 'patio' in command:
            message = message + "patio"
            GPIO.output(red, 1)
        if 'cocina' in command:
            message = message + "cocina"
            GPIO.output(green, 1)
        if 'all' in command:
            message =  message + "all"
            GPIO.output(blue, 1)   
            GPIO.output(yellow, 1)
            GPIO.otput(red, 1) 
            GPIO.output(green, 1)             

    message = message + "light(s)"
    telegram_bot.sendMessage(chat_id, message)

    if 'off' in command:
        message = 'off' 
        if 'sala' in command:
            message = message + "sala"
            GPIO.output(blue, 0)
        if 'comedor' in command:
            message = message + "comedor"
            GPIO.output(yellow, 0)
        if 'patio' in command:
            message = message + "patio"
            GPIO.otput(red, 0)
        if 'cocina' in command:
            message = message + "cocina"
            GPIO.output(green, 0)
        if 'all' in command:
            message =  message + "all"
            GPIO.output(blue, 0)   
            GPIO.output(yellow, 0)
            GPIO.otput(red, 0) 
            GPIO.output(green, 0)             

    message = message + "light(s)"
    telegram_bot.sendMessage(chat_id, message)

telegram_bot = telepot.Bot('1576472367:AAEGUfU1bBOtw_JN7v1LNBkKM67UsZbUkKE')   
print(telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running...')
while 1:
    time.sleep(10)
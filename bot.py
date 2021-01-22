from pygame import mixer
import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
green = 19
yellow = 6
red = 13
blue = 5

now = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

##LED Blue
GPIO.setup(blue, GPIO.OUT)
GPIO.output(blue, 0) #Off initially
#LED Yellow
GPIO.setup(yellow, GPIO.OUT)
GPIO.output(yellow, 0) #Off initially
#LED Red
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, 0) #Off initially
#LED green
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, 0) #Off initially
0
def action(msg):
	chat_id = msg['chat']['id']
	command = msg['text']

	print ('Received: %s' % command)
	message = "Comandos:"
	telegram_bot.sendMessage (chat_id, message)
	message = "all on \n all off \n sala on \n patio on \n cocina on \n comedor on \n sala off \n patio off \n cocina off \n comedor off "
	telegram_bot.sendMessage (chat_id, message)
	if 'on' in command:
		message = "on"
		if 'sala' in command:
			message = message + " Sala "
			GPIO.output(blue, 1)
		if 'comedor' in command:
			message = message + " Comedor "
			GPIO.output(yellow, 1)
		if 'patio' in command:
			message = message + " Patio "
			GPIO.output(red, 1)
		if 'cocina' in command:
			message = message + " Cocina "
			GPIO.output(green , 1)
		if 'all' in command:
			message = message + "all "
			GPIO.output(blue, 1)
			GPIO.output(yellow, 1)
			GPIO.output(red, 1)
			GPIO.output(green, 1)
		message = message + " lights "
		telegram_bot.sendMessage (chat_id, message)

	if 'off' in command:
		message = "off"
		if 'sala' in command:
			message = message + " Sala "
			GPIO.output(blue, 0)
		if 'comedor' in command:
			message = message + " Comedor "
			GPIO.output(yellow, 0)
		if 'patio' in command:
			message = message + " Patio "
			GPIO.output(red, 0)
		if 'cocina' in command:
			message = message + " Cocina "
			GPIO.output(green , 0)
		if 'all' in command:
			message = message + " all "
			GPIO.output(blue, 0)
			GPIO.output(yellow, 0)
			GPIO.output(red, 0)
			GPIO.output(green, 0)
	if 'music' in command :
		message = "Abriendo reproductor"
		telegram_bot.sendMessage (chat_id, message)
		message = "Seleciona una cancion"
		telegram_bot.sendMessage (chat_id, message)
		message = "1-Exile-Taylor Swift"
		telegram_bot.sendMessage (chat_id, message)
		message = message + "lights"
		telegram_bot.sendMessage (chat_id, message)
	if '1' in command :
		mixer.init()
		mixer.music.load('/home/pi/exile.mp3')
		mixer.music.set_volume(0.7)
		mixer.music.play()
		message = "p para pausar"
		telegram_bot.sendMessage (chat_id, message)
		message = "r para reanudar"
		telegram_bot.sendMessage (chat_id, message)
		message = "s para detener"
		telegram_bot.sendMessage (chat_id, message)
		message = "e elegir nueva"
		telegram_bot.sendMessage (chat_id, message)
	if 'p' in command :
		mixer.music.pause()
	if 'r' in command :
		mixer.music.unpause()
	if 's' in command :
		mixer.music.stop

telegram_bot = telepot.Bot('1576472367:AAEGUfU1bBOtw_JN7v1LNBkKM67UsZbUkKE')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running...')

while 1:
	time.sleep(10)

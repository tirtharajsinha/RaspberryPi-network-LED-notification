import requests
import RPi.GPIO as GPIO
import time
import atexit

isconnected=False
pin23state=False
internet_led=21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(internet_led,GPIO.OUT)

def connect(host="https://google.com"):
	try:
		requests.get(host,verify=False, timeout=2)
		
		return True
	except:
		return False
		
		
def exit_handler():
	GPIO.output(internet_led,GPIO.LOW)
	pin23state=False
	print("closing the netCheck Tool for raspberry pi")





while True:
	print("Checking connection : ")
	state=connect()
	if state:
		print("RPi is connected to internet : OK")
	else:
		print("RPi is not connected to internet : Not OK")
	if state and state != isconnected:
		GPIO.output(internet_led,GPIO.HIGH)
		pin23state=True
		isconnected=True
		time.sleep(10)
		GPIO.output(internet_led,GPIO.LOW)
		pin23state=False
	elif state and state==isconnected:
		time.sleep(2)
	elif not state:
		isconnected=False
		for i in range(4):
			if pin23state:
				GPIO.output(internet_led,GPIO.LOW)
				pin23state=False
			else:
				GPIO.output(internet_led,GPIO.HIGH)
				pin23state=True
				
			time.sleep(.5)
			
			
atexit.register(exit_handler)

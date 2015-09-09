import RPi.GPIO as GPIO
import time
import picamera
from iodpython.iodindex import IODClient
from twilio.rest import TwilioRestClient

import boto
from boto.s3.key import Key

conn = boto.connect_s3("AWS_API_KEY", "AWS_SECRET_KEY")
b = conn.get_bucket("hackathon-bell")

twilio_client = TwilioRestClient("TWILIO_API_KEY", "TWILIO_SECRET_KEY")
to_number = "TO_NUMBER"
from_number = "FROM_NUMBER"

client = IODClient("http://api.idolondemand.com/", "IOD_API_KEY")

camera = picamera.PiCamera()
#
camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 0
camera.video_stabilization = False
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
camera.rotation = 0
camera.hflip = False
camera.vflip = False
camera.crop = (0.0, 0.0, 1.0, 1.0)
#
time.sleep(0.5)
camera.capture('image1.jpg')

LED1_PIN = 4
LED2_PIN = 17
BUTTON_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1_PIN, GPIO.OUT) # setup 1st LED
GPIO.setup(LED2_PIN, GPIO.OUT) # setup 2nd LED
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

## initialize
print "Initializing..."
GPIO.output(LED1_PIN, True)
GPIO.output(LED2_PIN, True)
time.sleep(2)
GPIO.output(LED1_PIN, False)
GPIO.output(LED2_PIN, False)
time.sleep(2)
##

## repeat over and over again
while True:
	camera.capture('image1.jpg')
	r = client.post('detectfaces', files = {'file': open('./image1.jpg', 'rb')})
	print "------------"
	print "POST to IDOL"
	if len(r.json()['face']) > 0: # is there a face in the image
		print "Face(s) detected"
		GPIO.output(LED1_PIN, True) #turn light on
		input_state = GPIO.input(BUTTON_PIN)
		if input_state == False: # i.e. the button was pushed
			print('Button pressed')
			print('Saving to S3')
			GPIO.output(LED2_PIN, True)
			k = Key(b)
			k.key = 'image1_s3.jpg' # this is what you want to name it in S3
			k.set_contents_from_filename('image1.jpg') # this is name of the lcoal file
			k.set_acl('public-read')
			time.sleep(2) #make sure it actually gets up there
			message = twilio_client.messages.create(to=to_number, from_=from_number, body="Someone is looking for you!", media_url='https://s3-us-west-2.amazonaws.com/hackathon-bell/image1_s3.jpg') 
			GPIO.output(LED2_PIN, False)
			print "Sent text"
			
	else:
		print "No face(s) detected"	
		GPIO.output(LED1_PIN, False) # turn light off

print "Done"
GPIO.cleanup()


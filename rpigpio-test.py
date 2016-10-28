import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18,50)
pwm.start(7.5)

try:
  while True:
    pwm.ChangeDutyCycle(7.5)
    time.sleep(4)
    pwm.ChangeDutyCycle(2.5)
    time.sleep(4)
    pwm.ChangeDutyCycle(12.5)
    time.sleep(4) 
except KeyboardInterrupt:
  pwm.stop()
  GPIO.cleanup()

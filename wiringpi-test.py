import wiringpi

print "Testing..."
wiringpi.delay(1000)
print "..1.."
wiringpi.delay(1000)
print "..2.."
wiringpi.delay(1000)
print "...3!"
print "Testing under progress"

OUTPUT = 2
SERVO_G4 = 4

print "Setting up wiringPi"
wiringpi.wiringPiSetup()

print "Setting PWM Output on G4"
wiringpi.pinMode(4, 2)
wiringpi.softPwmCreate(SERVO_G4,0,100)

print "Going through PWM ranges"
for r in range(0,100):
  wiringpi.softPwmWrite(SERVO_G4,r)
  wiringpi.delay(100)

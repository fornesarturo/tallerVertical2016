import random
import time
import pyupm_buzzer as upmBuzzer
import pyupm_grove as grove
import pyupm_i2clcd as lcd

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
myLcd.setCursor(0,0)
# Create the button object using GPIO pin 3
button = grove.GroveButton(3)

#Buzzer object using GPIO pin 4
buzzer = upmBuzzer.Buzzer(4)

chords = [upmBuzzer.DO, upmBuzzer.RE, upmBuzzer.MI, upmBuzzer.FA, 
          upmBuzzer.SOL, upmBuzzer.LA, upmBuzzer.SI, upmBuzzer.DO, 
          upmBuzzer.SI];

# Make a DO sound if button value is True and change myLcd color to a random value.
contador = 0
myLcd.setCursor(0,0)
while 1:
	if button.value():
		myLcd.setColor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		print buzzer.playSound(chords[0], 1000000)
		contador += 1
    		
# Delete the buzzer object
del buzzer

# Delete the button object
del button

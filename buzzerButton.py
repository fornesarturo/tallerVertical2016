import time
import pyupm_buzzer as upmBuzzer
import pyupm_grove as grove

# Create the button object using GPIO pin 3
button = grove.GroveButton(3)

#Buzzer object using GPIO pin 4
buzzer = upmBuzzer.Buzzer(4)

chords = [upmBuzzer.DO, upmBuzzer.RE, upmBuzzer.MI, upmBuzzer.FA, 
          upmBuzzer.SOL, upmBuzzer.LA, upmBuzzer.SI, upmBuzzer.DO, 
          upmBuzzer.SI];

# Read the input and print status of the button and make a DO sound, waiting one second between readings.
while 1:
    print button.name(), ' value is ', button.value()
    print buzzer.playSound(chords[0], 1000000)
    time.sleep(1)

print "exiting application"

# Delete the buzzer object
del buzzer

# Delete the button object
del button

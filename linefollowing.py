
import ThunderBorg
import time
import sys
import RPi.GPIO as GPIO
global TB
global step
maxPower = 1.00
holdingPower = 0.50
sequence = [                            # Order for stepping 
        [+maxPower, +maxPower],
        [+maxPower, -maxPower],
        [-maxPower, -maxPower],
        [-maxPower, +maxPower]] 
sequenceHold = [                        # Order for stepping at holding power
        [+holdingPower, +holdingPower],
        [+holdingPower, -holdingPower],
        [-holdingPower, -holdingPower],
        [-holdingPower, +holdingPower]] 
stepDelay = 0.002    
TB = ThunderBorg.ThunderBorg()     # Create a new ThunderBorg object
TB.i2cAddress = 0x15              # Uncomment and change the value if you have changed the board address
TB.Init()                          # Set the board up (checks the board is connected)
if not TB.foundChip:
    boards = ThunderBorg.ScanForThunderBorg()
    if len(boards) == 0:
        print 'No ThunderBorg found, check you are attached :)'
    else:
        print 'No ThunderBorg at address %02X, but we did find boards:' % (TB.i2cAddress)
        for board in boards:
            print '    %02X (%d)' % (board, board)
        print 'If you need to change the I²C address change the setup line so it is correct, e.g.'
        print 'TB.i2cAddress = 0x%02X' % (boards[0])
    sys.exit()
step = -1
# Power settings
voltageIn = 12.0                        # Total battery voltage to the ThunderBorg
voltageOut = 12.0                       # Maximum motor voltage

# Setup the power limits
if voltageOut > voltageIn:
    maxPower = 1.0
else:
    maxPower = voltageOut / float(voltageIn)

# Show battery monitoring settings
battMin, battMax = TB.GetBatteryMonitoringLimits()
battCurrent = TB.GetBatteryReading()
print 'Battery monitoring settings:'
print '    Minimum  (red)     %02.2f V' % (battMin)
print '    Half-way (yellow)  %02.2f V' % ((battMin + battMax) / 2)
print '    Maximum  (green)   %02.2f V' % (battMax)
print
print '    Current voltage    %02.2f V' % (battCurrent)
print

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN)  # Left Line Sensor Reading
GPIO.setup(36, GPIO.IN)  # Right Line Sensor Reading
GPIO.setup(38, GPIO.IN)  # Middle Line Sensor Reading

print "Waiting For Sensor To Settle"
time.sleep(2)



def GetSensorReadings():
    print "Taking sensor readings"
    leftlinesensor = GPIO.input(40)
    middlelinesensor = GPIO.input(38)
    rightlinesensor = GPIO.input(36)
    print leftlinesensor
    print middlelinesensor
    print rightlinesensor
    return leftlinesensor, middlelinesensor, rightlinesensor


def Forward():
    TB.SetMotor1(5)
    TB.SetMotor2(5)

def Reverse():
    TB.SetMotor1(-5)
    TB.SetMotor2(-5)


def Right():
    TB.SetMotor1(5)
    TB.SetMotor2(-5)


def Left():
    TB.SetMotor1(-5)
    TB.SetMotor2(5)

try:
    while (True):
        leftlinesensor, middlelinesensor, rightlinesensor = GetSensorReadings()
        if leftlinesensor == 1 and rightlinesensor == 0:
            TB.SetMotor1(0)
            TB.SetMotor2(0)
            time.sleep(0.15)
            Right()
            time.sleep(0.15)
        elif rightlinesensor == 1 and leftlinesensor == 0:
            TB.SetMotor1(0)
            TB.SetMotor2(0)
            time.sleep(0.15)
            Left()
            time.sleep(0.15)
        else:
            Forward()

finally:
    TB.SetMotor1(0)
    TB.SetMotor2(0)
    print("Cleaning Up!")
    GPIO.cleanup()

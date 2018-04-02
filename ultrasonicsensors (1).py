#!/usr/bin/env python
# coding: latin-1

# Import the libraries we need
import UltraBorg
import time
import ThunderBorg
import sys
import RPi.GPIO as GPIO
global TB
global step

def turnLeft():
    print "Turning Left"
    TB.SetMotor1(0.6)
    TB.SetMotor2(0.1)
def turnRight():
    print "Turning Right"
    TB.SetMotor1(0.1)
    TB.SetMotor2(0.6)

def turnLeftKinda():
    print "Turning Left Kinda"
    TB.SetMotor1(0.6)
    TB.SetMotor2(0.4)

def turnRightKinda():
    print "Turning Right Kinda"
    TB.SetMotor1(0.4)
    TB.SetMotor2(0.6)


# Start the UltraBorg
UB = UltraBorg.UltraBorg()      # Create a new UltraBorg object
UB.Init()

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

try:
    while True:
        # Read all four ultrasonic values
        usm1 = UB.GetDistance1() #front
        usm2 = UB.GetDistance2() #right
        usm3 = UB.GetDistance3() #left

        # Convert to the nearest millimeter
        usm1 = int(usm1)
        usm2 = int(usm2)
        usm3 = int(usm3)
        # Display the readings
        if usm1 == 0:
            print '#1 No reading'
        else:
            print '#1 % 4d mm' % (usm1)
        if usm2 == 0:
            print '#2 No reading'
        else:
            print '#2 % 4d mm' % (usm2)
        if usm3 == 0:
            print '#3 No reading'
        else:
            print '#3 % 4d mm' % (usm3)
        
        print
        # Wait between readings
        #time.sleep(.5)

        if usm1 < 400 and usm3 < usm2:
            turnRight()
        elif usm3 < usm2:
            turnRightKinda()

        elif usm1 < 400 and usm2 < usm3:
            turnLeft()
        elif usm2 < usm3:
            turnLeftKinda()
                
        else:
            TB.SetMotors(0.6)
        
except KeyboardInterrupt:
    # User has pressed CTRL+C
    TB.MotorsOff()
    
    print 'Done'


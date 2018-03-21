#!/usr/bin/env python
# coding: latin-1

# Import the libraries we need
import UltraBorg
import time
import ThunderBorg
import sys

# Start the UltraBorg
UB = UltraBorg.UltraBorg()      # Create a new UltraBorg object
UB.Init()                       # Set the board up (checks the board is connected)

#insert thunderborg setup code here

# Loop over the sequence until the user presses CTRL+C
print 'Press CTRL+C to finish'
try:
    while True:

        #insert motor code here

        # Read all four ultrasonic values
        usm1 = UB.GetDistance1()
        usm2 = UB.GetDistance2()
        usm3 = UB.GetDistance3()
        usm4 = UB.GetDistance4()
        # Convert to the nearest millimeter
        usm1 = int(usm1)
        usm2 = int(usm2)
        usm3 = int(usm3)
        usm4 = int(usm4)
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
        if usm4 == 0:
            print '#4 No reading'
        else:
            print '#4 % 4d mm' % (usm4)
        print
        # Wait between readings
        time.sleep(.1)
    
        # Move motors

        if usm1 < 10: 
            
        else:

        if usm2 < 10::
            TB.MotorsOff() 
        else:

        if usm3 < 10: 
            
        else:

        if usm4 < 10: 
            
        else:



except KeyboardInterrupt:
    # User has pressed CTRL+C
    print 'Done'

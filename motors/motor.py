# Setup the library ready for use
import ThunderBorg                      # Load the library
TB = ThunderBorg.ThunderBorg()          # Create a board object
TB.Init()                               # Setup the board
 
# Setting motor speeds
TB.SetMotor1(power)                     # Set motor 1 speed
TB.SetMotor2(power)                     # Set motor 2 speed
TB.SetMotors(power)                     # Set speed of both motors
TB.MotorsOff()                          # Stop both motors
 
# Reading motor speeds
TB.GetMotor1()                          # Read motor 1 speed
TB.GetMotor2()                          # Read motor 2 speed
 
# Controlling the LED
TB.SetLed1(r, g, b)                     # Set the colour of the ThunderBorg LED (values from 0.0 to 1.0)
TB.GetLed1()                            # Read the colour of the ThunderBorg LED (values from 0.0 to 1.0)
TB.SetLed2(r, g, b)                     # Set the colour of the ThunderBorg Lid LED (values from 0.0 to 1.0)
TB.GetLed2()                            # Read the colour of the ThunderBorg Lid LED (values from 0.0 to 1.0)
TB.SetLeds(r, g, b)                     # Set the colour of both LEDs (values from 0.0 to 1.0)
 
# Battery monitoring
TB.SetLedShowBattery(enabled)           # Set if the LEDs reflect the current battery reading
TB.GetLedShowBattery()                  # Read if the LEDs reflect the current battery reading
TB.GetBatteryReading()                  # Read the current voltage level from the battery
TB.SetBatteryMonitoringLimits(min, max) # Set the limits for the LED based battery monitoring
TB.GetBatteryMonitoringLimits()         # Read the limits for the LED based battery monitoring
 
# Controlling the failsafe
TB.SetCommsFailsafe(enabled)            # Set if the communications failsafe is active
TB.GetCommsFailsafe()                   # Read if the communications failsafe is active
 
# Testing for faults
TB.GetDriveFault1()                     # See if there is a fault reported for M1
TB.GetDriveFault2()                     # See if there is a fault reported for M2
 
# RasPiO InsPiRing control
TB.SetExternalLedColours([[r,g,b], [r,g,b], [r,g,b], ..., [r,g,b]])
                                        # Set the colour of each LED on the InsPiRing (values from 0.0 to 1.0)
 
# Setting parameters (before Init)
TB.i2cAddress = address                 # Set the address of the board to use
TB.printFunction = function             # Re-route / disable diagnostic messages
 
# Reading parameters (after Init)
print TB.busNumber                      # Shows which I²C bus the board is connected on
print TB.foundChip                      # See if the board is found / not found
 
# Other functions
ThunderBorg.ScanForThunderBorg()        # Sweep the I²C bus for available boards
ThunderBorg.SetNewAddress(address)      # Configure the attached board with a new address
TB.Help()                               # Get help on the available functions

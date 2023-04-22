print("SIMPLE CRANE POSITION CONTROL PROGRAM")
print("This program is designed to allow or disallow gantry crane movement when it is in desired position. \
Program supposed to work by collecting signal from the measuring wheel giving information about current position")

print("SET NECESERY PARAMETERS: ")
railLen= int(input("complete crane rail lenght in cm: "))

railLenStr = str(railLen)

print("complete crane rail lenght = ",railLenStr , "cm")


firstStop = int(input("Set your first stop position. \
Crane will not be able to go before place you set (cm)"))

firstStopStr = str(firstStop)

print("Your choosen 1 stop position is: ", firstStopStr)

secondStop= int(input("Set your second stop place in cm. Crane will no able to go further"))

secondStopStr = str(secondStop)
print("Your choosen maximum acces is", secondStopStr , "cm")

x=0
while(x<1):
	position = int(input("input crane position taken from the measuring wheel signal. "))

	if(position<firstStop and position>0):
		print("moove backwards locked")
	elif(position>secondStop and position<railLen):
		print("moove forward locked")
	elif(position<0):
		print("LOCATION SYSTEM FAILURE: Try to restart crane power and make shure the measuring wheel works propertly. Otherwise call tech support. CRANE MOOVE OFF. To start the crane - run it in accident mode DO NOT OPERATE IF NOT NECESERY. Location system is being off while accident mode.")
	elif(position>railLen):
		print("LOCATION SYSTEM FAILURE: Try to restart crane power and make shure the measuring wheel works propertly. Otherwise call tech support. CRANE MOOVE OFF. To start the crane - run it in accident mode DO NOT OPERATE IF NOT NECESERY. Location system is being off while accident mode.")
	else:
		print("Crane move possible")

# command module for gradiometer

import vmcontrols.vmcontrols as vm
import fileinput.sm6read as sm6
import analysis.delta_analysis as delta
import fileinput.langparsing as parse
import stepper.motorcontrol as motor
from time import sleep, time
from datetime import datetime
from os import system

runstuff = False
testlength = 5 #seconds

def main():
	
	system('clear') # clear screen to start

	if runstuff:
		vm.startSpectramag6()

	sleep(5 * int(runstuff))

	meas = raw_input("Press enter to take a measurement, or type 'exit' to quit \n")

	while (meas != 'exit'):

		savedata = parse.ynPrompt('Would you like to save the data from this measurement?')
		# savegraphs = parse.ynPrompt('Would you like to save the graphs from this measurement?')

		# start fluxgates

		print "Verifying transfer dir clear"

		if runstuff:
			vm.guestClearTransferDir()

		sleep(5 * int(runstuff))

		print "Starting fluxgates"

		if runstuff:
			vm.startTest()

		sleep(5 * int(runstuff)) # for zeroing

		print "Starting motor at", datetime.fromtimestamp(time()).strftime('%H:%M')

		if runstuff:
			motor.runCycle()

		print "Stopping motor at", datetime.fromtimestamp(time()).strftime('%H:%M')

		sleep(5 * int(runstuff)) # buffer

		# now the measurement is done and the motor has stopped

		if runstuff:
			vm.saveInputs()

		sleep(10 * int(runstuff)) # extra buffer for read/write safeishness

		# do analysis here
		# currently delta analysis, but should be other in production

		if runstuff:
			in1 = sm6.readFile('/home/gradio/transferdir/')

		# now save data if desired

		if savedata:

			parse.sendFilesToCluster(['/home/mpalmer/test/nohup.out'], 1)

		sleep(10)

		system('clear') # clear screen to reset

		meas = raw_input("Press enter to take a measurement, or type 'exit' to quit \n")



if __name__ == '__main__':
	main()


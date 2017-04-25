# command module for gradiometer

import vmcontrols.vmcontrols as vm
import fileinput.sm6read as sm6
import analysis.delta_analysis as delta
import fileinput.langparsing as parse
import stepper.motorcontrol as motor
from time import sleep, time
from datetime import datetime
from os import system

runstuff = True
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

		print "Starting fluxgates"

		if runstuff:
			vm.startTest()

		sleep(5 * int(runstuff)) # for zeroing

		sleep(5 * int(runstuff)) # buffer

		if runstuff:
                    print 'Running motor'
	            motordata = motor.runInShield()

		sleep(5 * int(runstuff)) # buffer

		sleep(60 * int(runstuff)) # give fluxgates time to save

		# now the measurement is done and the motor has stopped

		if runstuff:
			vm.saveInputs()

		sleep(20 * int(runstuff)) # extra buffer for read/write safeishness

		# do analysis here
		# currently delta analysis, but should be other in production

		if runstuff:
                    print 'replace2'
			#in1 = sm6.readFile('/home/gradio/transferdir/')

		# now save data if desired

		if savedata:

			f = open('motordata', 'w')
			f.write('Motor start time: ' + str(motordata[0]))
			f.write('\n')
			f.write('Motor reversal time: ' + str(motordata[1]))
			f.write('\n')
			f.write('Motor stop time: ' + str(motordata[2]))
			f.write('\n')
			f.close()

			parse.sendFilesToCluster(['/home/gradio/transferdir/IN1.Dat', '/home/gradio/transferdir/IN2.Dat', 'motordata'], runstuff)

			system('rm -f motordata')

		sleep(3)

                vm.clearMeasurement()
                
                sleep(1)

	        system('clear') # clear screen to reset

            	meas = raw_input("Press enter to take a measurement, or type 'exit' to quit \n")



if __name__ == '__main__':
	main()


from os import system

print "Test"

system('xdotool search --name "Google Chrome" windowactivate && sleep 0.5 && xdotool click 1')

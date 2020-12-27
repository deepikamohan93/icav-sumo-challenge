import os, sys

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
	sys.exit("please declare environment variable 'SUMO_HOME'")
	sys.path.append(os.path.join('c:', os.sep, 'whatever', 'path', 'to', 'sumo', 'tools'))

sumoBinary = "/path/to/sumo-gui"
sumoCmd = [sumoBinary, "-c", "yourConfiguration.sumocfg"]

import traci
import traci.constants as tc

traci.start(["sumo-gui", "-c", "simulation-config.sumocfg"])

step=0
f= open('output.csv', 'w')
header=['Step','Vehicle','\tDistance', 'C02 emissions']
for t in header:
	f.write("%s," % t)

while traci.simulation.getMinExpectedNumber() > 0:

	for veh_id in traci.vehicle.getIDList():
		out= [step, veh_id, traci.vehicle.getDistance(veh_id), traci.vehicle.getCO2Emission(veh_id)]
		print(out)
		
		f.write("\n")
		for item in out:
			f.write("%s," % item)
	
	traci.simulationStep()

	step +=1
	
traci.close()
sys.stdout.flush()
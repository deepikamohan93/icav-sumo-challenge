# icav-sumo-challenge

Project
Microsimulation modeling using Sumo Platform and Python 3.9.1 for Portway- Cornishway, Woodhouse Park, Manchester 

Built with
1. Eclipse SUMO Version 1.6.0
2. Python 3.9.1

Steps to run simulation
1. Download files from the repository.
2. Open the command prompt window from the start menu. Type 'cmd' in the search box of the start menu and press enter. The command prompt window be opened with the directory set to the default directory. 
3. Change the directory of the command prompt to the downloaded folder ('sumo-files'). Open 'sumo-files' folder and copy the directory's path from the address at the top of the folder and type cd 'directory's path' in the command prompt and press enter. The directory will be changed to the project folder.
4. Type 'python sumo.py' in the command prompt and press enter. This simulation will be opened in the SUMO-GUI.
5. By default the delay is set to 0. This can result in a simulation that runs too fast to see any vehicles. Set the delay value to a sufficiently high value (say 200ms) so that the simulation is run with adequate timegap between simulation steps.
6. To run the simulation, click on the 'play' button on the tool bar or select Simulation > Play (Ctrl+A) from the menu bar. The simulation will start running with 200ms delay and will continue until the last vehicle leaves the network. Step by step estimates of distance travelled by the vehicle and CO2 emissions will be displayed in the command prompt along with the simulation run. 
On completion of the simulation a pop-up window will appear on the screen. Select 'yes' to close all open files and close the sumo-gui to view the output files. 
7. Go to 'sumo-files' folder and open 'output.csv' file to view the step by step estimates of distance travelled by the vehicle and CO2 emissions.

Simulation workflow
Input files
1. Network file- the traffic related part of the map (file name: network.xml). The network area covers the Portway- Cornishway surrounding the Woodhouse Park.
2. Traffic demand file- traffic demand of the network area is defined using this file. (file name: demand.rou.xml). A standard passenger car flow with maximum running speed of 13mps starting from Portway road completing one circle around the Woodhouse Park is defined in this file.
3. View Settings file- allows to change and customize the simulations' appearance and visualization: (file name: gui-settings.xml)

Output files
1. output.csv- Step by step estimates of distance travelled by the vehicle and CO2 emissions are recorded in this file

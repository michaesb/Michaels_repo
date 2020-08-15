# DJI Tello drone software for a PS-controller


This is a folder which contain the software for operating the both the drone and read messages from the PS3-controller.



## Software Requirements

This requires a Linux computer with ROS (robot operating system) in order to operate the PS-controller. You can run the simple commands

ROS can be installed and explained at http://wiki.ros.org/ROS/Tutorials


In addition to this you need to install http://wiki.ros.org/joy in order to run the joynode. This gives the input from the PS-controller as a ROS topic which the joystick controller listens to.

A PS-controller, both PS4 and PS3, connected to the computer with a USB connection is needed.

Xterm is also used here to open more terminals, since multiple programs need to run on the same time and it makes more manageable.

## USAGE

In order run the drone, press the on button on the right of the drone. Wait it for a blinking orange light and find the Wifi on the computer and connect to it.
Note that all commands below needs to be run in the main folder.
(~/Michael_repo/Dji_Tello_program/$)

### Drone only (without PS-controller)

If you would like to run this without the controller, i.e don't have a PS3-controller or need to debug some bugs,
you can run this RYZE test program instead:  


```python
python dji_tello_test.py
```

If it worked, it should jump to the next line. Here you can give it the commands manually typing it in the terminal and you can receive the response.
You'd want to first send it "command",(type only the letters), so it will take other commands. Then you can tell it to do other commands like "takeoff" and "land".
For a full list of all the commands see the the document: [RYZE robotics  commands](
https://dl-cdn.ryzerobotics.com/downloads/tello/0228/Tello+SDK+Readme.pdf?fbclid=IwAR2brujp0fihe8Ry2V768-AVAdF-wvtdA2Da04oglp7mm_dwafAtiiMI0sE)

### PS-controller (without the drone)
If you'd like to test the PS-controller, run the command underneath:

```bash
./run_scripts/run_PS_controller.sh
```
This will open three xterminals. One will be rosrun and is neceasery for other ros programs to run (small one in the corner). One will run the joynode which sends the PS-controller message through a topic (middle one). The last one listens to the topic sent by the joynode and prints the buttons and axes info (One on the right).

### Full system
In order to run both the PS-controller and the drone run:
```bash
./run_scripts/run_full_system.sh
```
Here you can use the controller to control the drone. To see the controls, see the layout in controller_layout.md


##Author:
Michael Bitney      
Josep Knutson,


## License
[MIT](https://choosealicense.com/licenses/mit/)

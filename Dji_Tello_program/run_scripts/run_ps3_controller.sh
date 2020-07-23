#!/bin/bash
xterm -T "roscore" -geometry 40x12+0+0 -hold -e "roscore"&
sleep 1
xterm -T "joynode" -geometry 80x24+900+0 -hold -e "rosrun joy joy_node"&
sleep 1
xterm -T "drone control" -geometry 800x240+2500+2500 -hold -e "python ps3_controller/src/joystick_control.py"&

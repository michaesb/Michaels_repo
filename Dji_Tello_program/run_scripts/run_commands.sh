#!/bin/bash
xterm -T "roscore" -geometry 40x12+0+0 -hold -e "roscore"&
sleep 1
xterm -T "listning to nodes" -geometry 80x24+450+0 -hold -e "python ps3_controller/src/PS3_test_node.py"&
sleep 0.1
xterm -T "joynode" -geometry 80x24+900+0 -hold -e "rosrun joy joy_node"&

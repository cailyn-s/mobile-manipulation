import rclpy, tf2_ros
from rclpy.node import Node
import hello_helpers.hello_misc as hm
import numpy as np

node = hm.HelloNode.quick_create('temp')

# Stow the robot
node.stow_the_robot()

# Extend arm and raise lift
node.move_to_pose({'joint_arm': 0.52}, blocking=True)
node.move_to_pose({'joint_lift': 1.1}, blocking=True)

# Rotate wrist in each direction, one at a time
node.move_to_pose({'joint_wrist_yaw': np.radians(45)}, blocking=True)
node.move_to_pose({'joint_wrist_pitch': np.radians(45)}, blocking=True)
node.move_to_pose({'joint_wrist_roll': np.radians(45)}, blocking=True)

# Open the gripper and close it

# Rotate the head

# Move back to stow

# Move forward 0.5 meters

# Rotate 180 degrees

# Move forward 0.5 meters again



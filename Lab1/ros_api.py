import rclpy, tf2_ros
from rclpy.node import Node
import hello_helpers.hello_misc as hm
import numpy as np
import time

node = hm.HelloNode.quick_create('temp')

# Stow the robot
node.stow_the_robot()

# Extend arm and raise lift
node.move_to_pose({'joint_arm': 0.52, 'joint_lift': 1.1}, blocking=True)

# Rotate wrist in each direction, one at a time
node.move_to_pose({'joint_wrist_roll': np.radians(-20)}, blocking=True)
time.sleep(0.1)
node.move_to_pose({'joint_wrist_roll': np.radians(20)}, blocking=True)
time.sleep(0.1)
node.move_to_pose({'joint_wrist_pitch': np.radians(15)}, blocking=True)
node.move_to_pose({'joint_wrist_yaw': np.radians(15)}, blocking=True)

# Open the gripper and close it
node.move_to_pose({'joint_gripper_finger_left': 1.0}, blocking=True)
node.move_to_pose({'joint_gripper_finger_left': 0.0}, blocking=True)

# Rotate the head
node.move_to_pose({'joint_head_pan': np.radians(20)}, blocking=True)
time.sleep(0.5)
node.move_to_pose({'joint_head_tilt': np.radians(-30)}, blocking=True)

# Move back to stow
node.stow_the_robot()

# Move forward 0.5 meters
node.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)

# Rotate 180 degrees
node.move_to_pose({'rotate_mobile_base': np.radians(180)}, blocking=True)

# Move forward 0.5 meters again
node.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)

node.destroy_node()
rclpy.shutdown()
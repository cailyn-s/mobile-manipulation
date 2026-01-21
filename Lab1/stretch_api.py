import stretch_body.robot
import numpy as np

robot = stretch_body.robot.Robot()
robot.startup()

# Stow the robot
robot.stow()
robot.push_command()
robot.wait_command()

# Extend arm and raise lift
robot.arm.move_to(0.52)
robot.lift.move_to(1.1)
robot.push_command()
robot.wait_command()

# Rotate wrist in each direction, one at a time
robot.end_of_arm.move_to('wrist_yaw', np.radians(30))
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('wrist_pitch', np.radians(30))
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('wrist_roll', np.radians(30))
robot.push_command()
robot.wait_command()

# Open the gripper and close it
robot.end_of_arm.move_to('stretch_gripper', 100) # open
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('stretch_gripper', -100) # closed
robot.push_command()
robot.wait_command()

# Rotate the head
robot.head.move_by('head_pan', np.radians(45)) # Move head pan
robot.head.move_by('head_tilt', np.radians(45)) # Move head tilt
robot.push_command()
robot.wait_command()

# Move back to stow
robot.stow()
robot.push_command()
robot.wait_command()

# Move forward 0.5 meters
robot.base.translate_by(0.5)
robot.push_command()
robot.wait_command()

# Rotate 180 degrees
robot.base.rotate_by(np.radians(180))
robot.push_command()
robot.wait_command()

# Move forward 0.5 meters again
robot.base.translate_by(0.5)
robot.push_command()
robot.wait_command()

robot.stop()
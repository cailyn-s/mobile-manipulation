# mobile-manipulation
3 terminal windows:
`ros2 launch stretch_core stretch_driver.launch.py`

`ros2 run rviz2 rviz2 -d `ros2 pkg prefix --share
stretch_calibration`/rviz/stretch_simple_test.rviz`

`ros2 launch stretch_core d435i_low_resolution.launch.py`

`ros2 topic info /stretch/joint_states`

`ros2 topic echo /joint_limits`
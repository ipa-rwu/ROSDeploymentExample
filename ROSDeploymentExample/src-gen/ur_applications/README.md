# ur_applications

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- lifcyclenode_manager
- bt_operator
- aruco_marker_publisher
- moveit_skill_server
- moveit_config_loader
- ur_io_control_gripper_skill_server
- realsence_tf_node
- driver
- robot_state_publisher_node
- controller_manager
- initial_joint_controller
- initial_joint_controller_spawner_stopped
- ur_ros2_control_node
- dashboard_client
- urscript_interface
- controller_stopper

The listed nodes offer the following connections:
- ActionServer: start_application [man2_msgs/RunApplication]
- Publisher: pub_aruco_markers [aruco_msgs/MarkerArray]
- Subscriber: get_image_raw [sensor_msgs/Image]
- ActionServer: compute_path_to_pose_skill [moveit_skills/ComputePathToPose]
- ActionServer: compute_path_to_point_skill [moveit_skills/ComputePathToPoint]
- ActionServer: compute_path_to_state_skill [moveit_skills/ComputePathToState]
- ActionServer: execute_trajectory_skill [moveit_skills/ExecuteTrajectory]
- ActionServer: get_current_ik_frame_pose_skill [moveit_skills/GetCurrentIKFramePose]
- ServiceServer: reload_parameters [std_srvs/Trigger]

## Installation

### Using release

This package can be copied to a valid ROS 2 workspace. To be sure that all the related dependencies are intalles the command **rosdep install** can be used.
Then the workspace must be compiled using the common ROS 2 build command:

```
mkdir -p ros2_ws/src
cd ros2_ws/
cp -r PATHtoTHISPackage/ur_applications src/.
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```


### From source code
```
mkdir -p ros2_ws/src
cd ros2_ws/
git clone https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver.gitgit clone https://github.com/UniversalRobots/Universal_Robots_ROS2_Drivergit clone https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```

## Usage


To execute the launch file, the following command can be called:

```
ros2 launch ur_applications ur_applications.launch.py lifcyclenode_manager/node_sequence:=[moveit_config_server, bt_operator, ur_io_control_gripper_skill_server, moveit_skill_server] bt_operator/customized_plugin_lib_names.ur_robot_skill_clients:=[io_control_gripper, get_ur_robot_state, get_ur_safety_state, get_ur_program_state, check_safety_mode, check_robot_mode, is_robot_running, is_safety_normal, is_program_running] bt_operator/default_plugin_lib_names:=[util_plugin_print_value] moveit_config_server/robot_name:=ur5e_workcell moveit_config_server/moveit_config_pkg:=ur5e_cell_moveit_config 
```

The generated launch files requires the xterm package, it can be installed by:

```
sudo apt install xterm
```




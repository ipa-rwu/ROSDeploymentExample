# moveit_skill_server

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- moveit_skill_server
- moveit_config_loader

The listed nodes offer the following connections:
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
cp -r PATHtoTHISPackage/moveit_skill_server src/.
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```


### From source code
```
mkdir -p ros2_ws/src
cd ros2_ws/
git clone https://gitlab.cc-asp.fraunhofer.de/ipa326/demonstrator/bt_based_application_framework.gitgit clone https://gitlab.cc-asp.fraunhofer.de/ipa326/demonstrator/bt_based_application_framework
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```

## Usage


To execute the launch file, the following command can be called:

```
ros2 launch moveit_skill_server moveit_skill_server.launch.py 
```

The generated launch files requires the xterm package, it can be installed by:

```
sudo apt install xterm
```




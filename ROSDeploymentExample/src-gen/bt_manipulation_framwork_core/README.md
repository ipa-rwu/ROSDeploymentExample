# bt_manipulation_framwork_core

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- lifcyclenode_manager
- bt_operator

The listed nodes offer the following connections:
- ActionServer: start_application [man2_msgs/RunApplication]

## Installation

### Using release

This package can be copied to a valid ROS 2 workspace. To be sure that all the related dependencies are intalles the command **rosdep install** can be used.
Then the workspace must be compiled using the common ROS 2 build command:

```
mkdir -p ros2_ws/src
cd ros2_ws/
cp -r PATHtoTHISPackage/bt_manipulation_framwork_core src/.
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```


### From source code
```
mkdir -p ros2_ws/src
cd ros2_ws/
git clone https://gitlab.cc-asp.fraunhofer.de/ipa326/demonstrator/bt_based_application_framework.git -b v1.0.0
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```

## Usage


To execute the launch file, the following command can be called:

```
ros2 launch bt_manipulation_framwork_core bt_manipulation_framwork_core.launch.py 
```

The generated launch files requires the xterm package, it can be installed by:

```
sudo apt install xterm
```




from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution, TextSubstitution

def generate_launch_description():
  ld = LaunchDescription()
  
  # *** PARAMETERS ***

  # *** ROS 2 nodes ***
  ur_io_control_gripper_skill_server = Node(
    package="ur_io_control_gripper_skill",
    executable="main_ur_io_control_gripper_action_server",
    prefix = 'xterm -e',
    output='screen',
    name="ur_io_control_gripper_skill_server"
  )

  # *** ROS 2 subsystems (include launch files)***

  # *** Add actions ***
  ld.add_action(ur_io_control_gripper_skill_server)

  return ld

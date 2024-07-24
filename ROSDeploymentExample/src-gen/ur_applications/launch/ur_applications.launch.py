from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution, TextSubstitution

def generate_launch_description():
  ld = LaunchDescription()
  
  # *** PARAMETERS ***

  # *** ROS 2 nodes ***

  # *** ROS 2 subsystems (include launch files)***
  include_bt_manipulation_framwork_core= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([ get_package_share_directory('bt_manipulation_framwork_core') + '/launch/bt_manipulation_framwork_core.launch.py'])
  )
  include_aruco_marker_detection_skill_server= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([ get_package_share_directory('aruco_marker_detection_skill_server') + '/launch/aruco_marker_detection_skill_server.launch.py'])
  )
  include_moveit_skill_server= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([ get_package_share_directory('moveit_skill_server') + '/launch/moveit_skill_server.launch.py'])
  )
  include_control_ur_gripper_via_io_skill= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([ get_package_share_directory('control_ur_gripper_via_io_skill') + '/launch/control_ur_gripper_via_io_skill.launch.py'])
  )
  include_realsense_camera_calibrated= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([get_package_share_directory('realsense_camera_calibrated') + '/launch/realsense_camera_calibrated.py'])
  )
  include_ur_control= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([get_package_share_directory('ur_robot_driver') + '/launch/ur_control.launch.py'])
  )

  # *** Add actions ***
  ld.add_action(include_bt_manipulation_framwork_core)
  ld.add_action(include_aruco_marker_detection_skill_server)
  ld.add_action(include_moveit_skill_server)
  ld.add_action(include_control_ur_gripper_via_io_skill)
  ld.add_action(include_realsense_camera_calibrated)
  ld.add_action(include_ur_control)

  return ld

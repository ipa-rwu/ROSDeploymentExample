import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution, TextSubstitution

def generate_launch_description():
  ld = LaunchDescription()
  
  # *** PARAMETERS ***
  moveit_skill_server_config = os.path.join(
    get_package_share_directory('moveit_skill_server'),
    'config',
    'moveit_skill_server.yaml'
  )
  robot_name_arg = DeclareLaunchArgument(
    "robot_name", default_value=TextSubstitution(text="TODO")
  )
  ld.add_action(robot_name_arg)
  moveit_pkg_name_arg = DeclareLaunchArgument(
    "moveit_pkg_name", default_value=TextSubstitution(text="TODO")
  )
  ld.add_action(moveit_pkg_name_arg)

  # *** ROS 2 nodes ***
  moveit_skill_server = Node(
    package="moveit_skills",
    executable="moveit_skill_server_node",
    prefix = 'xterm -e',
    output='screen',
    name="moveit_skill_server",
    remappings=[
      ("compute_path_to_pose", "compute_path_to_pose_skill"),
      ("compute_path_to_point", "compute_path_to_point_skill"),
      ("compute_path_to_state", "compute_path_to_state_skill"),
      ("execute_trajectory", "execute_trajectory_skill"),
      ("get_current_ik_frame_pose", "get_current_ik_frame_pose_skill")]
    ,
    parameters = [moveit_skill_server_config]
  )
  moveit_config_loader = Node(
    package="moveit_skills",
    executable="moveit_config_server",
    prefix = 'xterm -e',
    output='screen',
    name="moveit_config_loader",
    remappings=[
      ("reload_parameters", "reload_parameters")]
    ,
    parameters=[{
    "robot_name": LaunchConfiguration("robot_name"),
    "moveit_config_pkg": LaunchConfiguration("moveit_pkg_name"),}]
  )

  # *** ROS 2 subsystems (include launch files)***

  # *** Add actions ***
  ld.add_action(moveit_skill_server)
  ld.add_action(moveit_config_loader)

  return ld

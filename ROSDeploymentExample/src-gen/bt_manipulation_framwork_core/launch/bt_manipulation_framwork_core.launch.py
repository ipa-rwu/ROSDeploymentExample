from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution, TextSubstitution

def generate_launch_description():
  ld = LaunchDescription()
  
  # *** PARAMETERS ***
  node_sequence_arg = DeclareLaunchArgument(
    "node_sequence", default_value=TextSubstitution(text="[bt_operator]")
  )
  ld.add_action(node_sequence_arg)
  load_bt_plugins_arg = DeclareLaunchArgument(
    "load_bt_plugins", default_value=TextSubstitution(text="[detect_aruco_marker_client, compute_path_to_state_client, compute_path_to_pose_client, compute_path_to_point_client, execute_trajectory_client, set_path_constraints_client, get_current_ik_frame_pose_client, print_value, update_pose]")
  )
  ld.add_action(load_bt_plugins_arg)
  use_sim_time_arg = DeclareLaunchArgument(
    "use_sim_time", default_value=TextSubstitution(text="false")
  )
  ld.add_action(use_sim_time_arg)

  # *** ROS 2 nodes ***
  lifcyclenode_manager = Node(
    package="nav2_lifecycle_manager",
    executable="lifecycle_manager",
    prefix = 'xterm -e',
    output='screen',
    name="lifcyclenode_manager",
    parameters=[{
    "node_names": LaunchConfiguration("node_sequence"),}]
  )
  bt_operator = Node(
    package="man2_bt_operator",
    executable="bt_operator",
    prefix = 'xterm -e',
    output='screen',
    name="bt_operator",
    remappings=[
      ("start_application", "start_application")]
    ,
    parameters=[{
    "customized_plugin_lib_names.man2_bt_skill_clients": LaunchConfiguration("load_bt_plugins"),
    "use_sim_time": LaunchConfiguration("use_sim_time"),}]
  )

  # *** ROS 2 subsystems (include launch files)***

  # *** Add actions ***
  ld.add_action(lifcyclenode_manager)
  ld.add_action(bt_operator)

  return ld

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution, TextSubstitution

def generate_launch_description():
  ld = LaunchDescription()
  
  # *** PARAMETERS ***
  camera_frame_arg = DeclareLaunchArgument(
    "camera_frame", default_value=TextSubstitution(text="")
  )
  ld.add_action(camera_frame_arg)
  reference_frame_arg = DeclareLaunchArgument(
    "reference_frame", default_value=TextSubstitution(text="")
  )
  ld.add_action(reference_frame_arg)
  marker_size_arg_arg = DeclareLaunchArgument(
    "marker_size_arg", default_value=TextSubstitution(text="0.0")
  )
  ld.add_action(marker_size_arg_arg)
  raw_image_topic_arg = DeclareLaunchArgument(
    "raw_image_topic", default_value=TextSubstitution(text="")
  )
  ld.add_action(raw_image_topic_arg)
  camera_info_topic_arg = DeclareLaunchArgument(
    "camera_info_topic", default_value=TextSubstitution(text="")
  )
  ld.add_action(camera_info_topic_arg)

  # *** ROS 2 nodes ***
  aruco_marker_publisher = Node(
    package="aruco_ros",
    executable="marker_publisher",
    prefix = 'xterm -e',
    output='screen',
    name="aruco_marker_publisher",
    remappings=[
      ("markers", "pub_aruco_markers"),
      ("image_raw", "get_image_raw")]
    ,
    parameters=[{
    "camera_frame": LaunchConfiguration("camera_frame"),
    "reference_frame": LaunchConfiguration("reference_frame"),
    "marker_size": LaunchConfiguration("marker_size_arg"),
    "raw_image_topic": LaunchConfiguration("raw_image_topic"),
    "camera_info_topic": LaunchConfiguration("camera_info_topic"),}]
  )

  # *** ROS 2 subsystems (include launch files)***

  # *** Add actions ***
  ld.add_action(aruco_marker_publisher)

  return ld

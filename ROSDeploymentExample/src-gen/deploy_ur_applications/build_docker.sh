#!/bin/bash
# Auto-generated script to search for folders and copy them

# Get the directory of the current script
current_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Iterate through all assignments in the plan
assignment_name="bt_framework"
echo "Processing assignment: $assignment_name"

  # Iterate through software components in the assignment
  sw_name="bt_manipulation_framwork_core"
  echo "Looking for folder: $sw_name"

  # Search for the folder with a package.xml file in the parent of the parent of the current directory
  found_folder=$(find "$current_dir/.." -type d -name "$sw_name" -exec test -f "{}/package.xml" \; -print | head -n 1)

  if [ -n "$found_folder" ]; then
    echo "Found folder: $found_folder"
    target_folder="$current_dir/$assignment_name"
    mkdir -p "$target_folder"
    cp -r "$found_folder" "$target_folder"
    echo "Copied $found_folder to $target_folder"
  else
    echo "Folder $sw_name with package.xml not found"
  fi
  sw_name="moveit_skill_server"
  echo "Looking for folder: $sw_name"

  # Search for the folder with a package.xml file in the parent of the parent of the current directory
  found_folder=$(find "$current_dir/.." -type d -name "$sw_name" -exec test -f "{}/package.xml" \; -print | head -n 1)

  if [ -n "$found_folder" ]; then
    echo "Found folder: $found_folder"
    target_folder="$current_dir/$assignment_name"
    mkdir -p "$target_folder"
    cp -r "$found_folder" "$target_folder"
    echo "Copied $found_folder to $target_folder"
  else
    echo "Folder $sw_name with package.xml not found"
  fi
  sw_name="control_ur_gripper_via_io_skill"
  echo "Looking for folder: $sw_name"

  # Search for the folder with a package.xml file in the parent of the parent of the current directory
  found_folder=$(find "$current_dir/.." -type d -name "$sw_name" -exec test -f "{}/package.xml" \; -print | head -n 1)

  if [ -n "$found_folder" ]; then
    echo "Found folder: $found_folder"
    target_folder="$current_dir/$assignment_name"
    mkdir -p "$target_folder"
    cp -r "$found_folder" "$target_folder"
    echo "Copied $found_folder to $target_folder"
  else
    echo "Folder $sw_name with package.xml not found"
  fi
assignment_name="launch_realsense"
echo "Processing assignment: $assignment_name"

  # Iterate through software components in the assignment
  sw_name="realsense_camera_calibrated"
  echo "Looking for folder: $sw_name"

  # Search for the folder with a package.xml file in the parent of the parent of the current directory
  found_folder=$(find "$current_dir/.." -type d -name "$sw_name" -exec test -f "{}/package.xml" \; -print | head -n 1)

  if [ -n "$found_folder" ]; then
    echo "Found folder: $found_folder"
    target_folder="$current_dir/$assignment_name"
    mkdir -p "$target_folder"
    cp -r "$found_folder" "$target_folder"
    echo "Copied $found_folder to $target_folder"
  else
    echo "Folder $sw_name with package.xml not found"
  fi
assignment_name="aruco_marker_publish"
echo "Processing assignment: $assignment_name"

  # Iterate through software components in the assignment
  sw_name="aruco_marker_detection_skill_server"
  echo "Looking for folder: $sw_name"

  # Search for the folder with a package.xml file in the parent of the parent of the current directory
  found_folder=$(find "$current_dir/.." -type d -name "$sw_name" -exec test -f "{}/package.xml" \; -print | head -n 1)

  if [ -n "$found_folder" ]; then
    echo "Found folder: $found_folder"
    target_folder="$current_dir/$assignment_name"
    mkdir -p "$target_folder"
    cp -r "$found_folder" "$target_folder"
    echo "Copied $found_folder to $target_folder"
  else
    echo "Folder $sw_name with package.xml not found"
  fi
assignment_name="ur_driver"
echo "Processing assignment: $assignment_name"

  # Iterate through software components in the assignment
  sw_name="ur_control"
  echo "Looking for folder: $sw_name"

  # Search for the folder with a package.xml file in the parent of the parent of the current directory
  found_folder=$(find "$current_dir/.." -type d -name "$sw_name" -exec test -f "{}/package.xml" \; -print | head -n 1)

  if [ -n "$found_folder" ]; then
    echo "Found folder: $found_folder"
    target_folder="$current_dir/$assignment_name"
    mkdir -p "$target_folder"
    cp -r "$found_folder" "$target_folder"
    echo "Copied $found_folder to $target_folder"
  else
    echo "Folder $sw_name with package.xml not found"
  fi

docker compose -f builder.docker-compose.yml build --no-cache

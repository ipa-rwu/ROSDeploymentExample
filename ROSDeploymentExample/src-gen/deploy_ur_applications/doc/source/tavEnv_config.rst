.. _tavEnv_config:

#################################
Target Environment Configuration
#################################


Check device configurations
#################################

* Configured properties for Device: "cmh_tower_400":

  .. list-table:: Configured properties for Device: "cmh_tower_400"

    * - property name
      - value

    * - os_name
      - ubuntu
    * - os_version
      - focal
    * - processor_architecture
      - x86

* Configured properties for Device: "arm":

  .. list-table:: Configured properties for Device: "arm"

    * - property name
      - value

    * - device_type
      - ur5e

* Configured properties for Device: "gripper":

  There are no properties defined for Device: "gripper"
* Configured properties for Device: "camera_realsense":

  .. list-table:: Configured properties for Device: "camera_realsense"

    * - property name
      - value

    * - device_type
      - d435
    * - device_name
      - camera
    * - serial_number
      - 920312073127


Check communication connection between devices
###############################################

* arm, gripperand are connected via **Io_tip**

* arm, cmh_tower_400and are connected via **Ethernet**

* cmh_tower_400, camera_realsenseand are connected via **Usb_01**


Check configurations for Device: "cmh_tower_400" are as follows:

  For Ethernet:

  .. code-block::
  
     IP address: 192.168.56.1
     Subnet mask: 255.255.255.0
     gateway: 192.168.56.1
     DNS server: 0.0.0.0



  For USB_01:

  .. code-block::
  
     Volumes:
       - /dev/video0
       - /dev/video1
       - /dev/video2
       - /dev/video3
       - /dev/video4
       - /dev/video5
Check configurations for Device: "arm" are as follows:



  For Ethernet:

  .. code-block::
  
     IP address: 192.168.56.2
     Subnet mask: 255.255.255.0
     gateway: 192.168.56.1
     DNS server: 0.0.0.0

Check configurations for Device: "gripper" are as follows:


Check configurations for Device: "camera_realsense" are as follows:



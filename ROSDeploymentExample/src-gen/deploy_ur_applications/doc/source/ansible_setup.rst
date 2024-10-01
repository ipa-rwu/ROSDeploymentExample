.. _ansible_setup:

############################
Setup Ansible
############################

Ansible automates the management of remote systems and controls their desired state.
A basic Ansible environment has three main components:


Control node
   A system on which Ansible is installed.
   You run Ansible commands such as ``ansible`` or ``ansible-inventory`` on a control node.

Managed node
   A remote system, or host, that Ansible controls.

Inventory
   A list of managed nodes that are logically organized.
   You create an inventory on the control node to describe host deployments to Ansible.

If you did not install Ansible yet, you can install it as follows:

#. Install Ansible:

   .. code-block:: bash

      python3 -m pip install --user ansible

#. Fill an inventory by adding the IP address, username (default ``anisble``) and also add IP address in ``/etc/ansible/hosts``.
   The following example adds the IP addresses of three virtual machines in KVM:

   .. code-block:: bash

   192.168.1.11 ansible_user=user_name

#. Verify the hosts in your inventory.

   .. code-block:: bash

      ansible all --list-hosts

#. Set up SSH connections so Ansible can connect to the managed nodes.

   a. Add your public SSH key to the ``authorized_keys`` file (path: ``.ssh/authorized_keys``) on each remote system as follow:

      * cmh_tower_400

   b. Test the SSH connections, for example:

   .. code-block:: bash

      ssh username@192.0.2.50

   If the username on the control node is different on the host, you need to pass the ``-u`` option with the ``ansible`` command.

#. Ping the managed nodes.

   .. code-block:: bash

      ansible all -m ping

#. Add and encrypt "sudo passward"

    To run containers with docker, we need to ensure docker is installed in each remote system.
    Therefore, it needs ''sudo password'' to perform that. ''sudo password'' will be encrypted!

    To do so, you can run:

   .. code-block:: bash

      ansible-vault create vars/cmh_tower_400/passwords.yml


    It requires you to provide a password that you will use to edit your passwords.

    After creating files, now you provide your ''sudo password'' by

   .. code-block:: bash

      ansible-vault edit vars/cmh_tower_400/passwords.yaml


    In each file, you need to enter as follows:

   .. code-block:: bash

      cmh_tower_400_sudo: "sudo password"


#. Start application.

   .. code-block:: bash

      ansible-playbook -i inventory.yaml playbook.yaml --ask-vault-pass --extra-vars '@vars/cmh_tower_400/passwords.yml' --verbose

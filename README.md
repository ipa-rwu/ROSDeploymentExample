# ROSDeploymentExample

Examples for using deployment tool

## src-gen folder structure

- `deploy_ur_applications`
  - [`ansible`](ROSDeploymentExample/src-gen/deploy_ur_applications/ansible): use Ansible for deploying
  - software components or subsystem defined in [`pick_and_place_ur5e_cell.planros`](ROSDeploymentExample/plan/pick_and_place_ur5e_cell.planros)
    - [`aruco_marker_publish`](ROSDeploymentExample/src-gen/deploy_ur_applications/aruco_marker_publish)
    - [`bt_framework`](ROSDeploymentExample/src-gen/deploy_ur_applications/bt_framework)
    - [`launch_realsense`](ROSDeploymentExample/src-gen/deploy_ur_applications/launch_realsense)
    - [`ur_driver`](ROSDeploymentExample/src-gen/deploy_ur_applications/ur_driver)
  - [cmh_tower_400](ROSDeploymentExample/src-gen/deploy_ur_applications/cmh_tower_400): the device where software will be deployed
  - [github](ROSDeploymentExample/src-gen/deploy_ur_applications/github): configuration for using github to build docker images
  - [gitlab](ROSDeploymentExample/src-gen/deploy_ur_applications/gitlab): configuration for using github to build docker images
  - [builder.docker-compose.yml](ROSDeploymentExample/src-gen/deploy_ur_applications/builder.docker-compose.yml): build docker images locally

## How to

### Build docker image locally

- build docker images for all software components
  ```
  cd src-gen/deploy_ur_applications
  docker compose -f builder.docker-compose.yml build
  ```
- build docker images for specified software components
  ```
  cd src-gen/deploy_ur_applications
  docker compose -f builder.docker-compose.yml build bt_framework ur_driver
  ```

### Launch software:

```
cd src-gen/deploy_ur_applications/cmh_tower_400
docker compose -f docker-compose.yaml up
```

### use Ansible for deployment

check document
[ansible_setup.rst](ROSDeploymentExample/src-gen/deploy_ur_applications/doc/source/ansible_setup.rst)
or chapter 3 in [deploy_ur_applications.pdf](ROSDeploymentExample/src-gen/deploy_ur_applications/doc/deploymentdocumentationfordeploy_ur_applications.pdf)

### Compile generated doc locally

```
# use Sphinx-build
cd doc
make latex
# check ".tex" in build/latex
./latex_command.sh pdflatex deploymentdocumentationfordeploy_ur_applications.tex
```

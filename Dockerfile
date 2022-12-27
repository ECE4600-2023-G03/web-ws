FROM ros:humble

RUN apt-get update

RUN apt update && \
    apt install -y \
    ros-humble-desktop \
    ros-humble-ros-base \
    ros-dev-tools

RUN apt update && \
    apt install -y \
    net-tools \
    tree \
    nano \
    vim \
    sqlite3 \
    python3-pip

RUN pip install setuptools==58.2.0

RUN apt install -y \
    ros-humble-turtlesim -y \
    ~nros-humble-rqt* -y \
    ros-humble-rviz2
    # ros-humble-gazebo-ros-pkgs

RUN apt install -y \
    python3-colcon-common-extensions \
    ros-humble-rosbridge-server -y \
    ros-humble-async-web-server-cpp -y 
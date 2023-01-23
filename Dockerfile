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
    curl \
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

# Install Node.js
RUN curl --silent --location https://deb.nodesource.com/setup_19.x | sudo -E bash -
RUN apt-get install --yes nodejs
RUN apt-get install --yes build-essential

# Binds to port 3000
EXPOSE  3000

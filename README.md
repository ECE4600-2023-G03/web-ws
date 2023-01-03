# web-ws

## Setup 
- build docker container: `./docker_build.sh`
- run docker container: `./docker_run.sh`
- source underlay: `source source.sh`
- in the `/web-ws` directory, create a `/src` folder
  - clone web_video_server package: `git clone -b ros2 https://github.com/RobotWebTools/web_video_server`
  - clone the simple publisher/subcriber from [ros2 tutorial](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html) (for String message testing)
- navigate back to `/web-ws` directory
  - `colcon build --symlink-install`
- deprecated errors of the web_video_server package are ok

## Launch file
- run: `ros2 launch launch/launch_all.py`
- This launch file launches:
  - two middlewares
    - web_video_server (`ros2 run web_video_server web_video_server`)
    -  rosbridge (`ros2 launch rosbridge_server rosbridge_websocket_launch.xml`)
  - a rosbag (shared for all team members in Onedrive): `ros2 bag play -l <rosbag_name>`
  - simple publisher node for String message with counter
  - publish a Twist message 
  - publish an Int16 message (number of balls)
  - publish a Bool message (on/off)
  - a turtlesim node & change its background rgb values


## Node JS
- Run NodeJS from the docker container: `node app.js`


## Access website:
- check IP address of the host: `ifconfig` for Linux
- NodeJS runs on port 3000
- Open a web browser, type on address bar: `<HostIP>:3000`
# web-ws

## Setup 
- build docker container
- run docker container
- source underlay
- in the /web-ws directory, create a `/src` folder
- clone web_video_server package: `git clone -b ros2 https://github.com/RobotWebTools/web_video_server`
- navigate back to /web-ws directory
- `colcon build --symlink-install`
- deprecated errors of the web_video_server package are ok

## Two middlewares
- run web_video_server: `ros2 run web_video_server web_video_server`
- run rosbridge: `ros2 launch rosbridge_server rosbridge_websocket_launch.xml`


## Node JS
- Install NodeJS LTS version [here](https://nodejs.org/en/)
- Run NodeJS on host: `node app.js`


## Testing message types
- video stream, run a rosbag (shared in Onedrive): `ros2 bag play -l <rosbag_name>`
- string message (std_msgs/String): `ros2 topic pub /my_topic std_msgs/String "data: HELLO WORLD"` 
- twist (speed)
- boolean (on/off)
- number of balls


## Access website:
- check IP address of the host
- NodeJS runs on port 3000
- Open a web browser, type on address bar: `<HostIP>:3000`
docker run \
-it \
--rm \
--name webws \
--env="DISPLAY" \
--env="QT_X11_NO_MITSHM=1" \
--volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
--net=host \
-e ROS_DOMAIN_ID=2  \
--entrypoint /bin/bash \
-v $(pwd):/home/web-ws/ \
-w /home/web-ws/ \
sim:web
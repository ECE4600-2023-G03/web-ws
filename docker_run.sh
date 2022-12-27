docker run \
-it \
--rm \
--name cam \
--env="DISPLAY" \
--env="QT_X11_NO_MITSHM=1" \
--volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
--net=host \
-e ROS_DOMAIN_ID=2  \
--entrypoint /bin/bash \
-v $(pwd):/home/cam-ws/ \
-w /home/cam-ws/ \
sim:camera
import os, sys

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from launch.substitutions import TextSubstitution
from launch.substitutions import LaunchConfiguration



def generate_launch_description():

    # args that can be set from the command line or a default will be used
    background_r_launch_arg = DeclareLaunchArgument(
        "background_r", default_value=TextSubstitution(text="100")
    )
    background_g_launch_arg = DeclareLaunchArgument(
        "background_g", default_value=TextSubstitution(text="100")
    )
    background_b_launch_arg = DeclareLaunchArgument(
        "background_b", default_value=TextSubstitution(text="100")
    )


    turtlesim = Node(
            package='turtlesim',
            executable='turtlesim_node',
            parameters=[{
                "background_r": LaunchConfiguration('background_r'),
                "background_g": LaunchConfiguration('background_g'),
                "background_b": LaunchConfiguration('background_b'),
            }]
        )

    # ros2 run web_video_server web_video_server
    web_video_server = Node(
            package='web_video_server',
            executable='web_video_server',
        )

    # include xml launch file
    rosbridge = IncludeLaunchDescription(
        XMLLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("rosbridge_server"),
                "launch/rosbridge_websocket_launch.xml",
            )
        )
    )

    # ros2 bag play -l rgb_640_15fps/
    camera = ExecuteProcess(
                cmd=[
                    "ros2",
                    "bag",
                    "play",
                    "--loop",
                    "rgb_640_15fps/rgb_640_15fps_0.db3",
                ],
            )

    # ros2 topic pub /string_topic std_msgs/String "data: Hello there" -1
    # string_topic = ExecuteProcess(
    #             cmd=[
    #                 "ros2",
    #                 "topic",
    #                 "pub",
    #                 "/string_topic",
    #                 "std_msgs/String",
    #                 "data: Hello there",
    #                 # "-1"
    #             ],
    #         )

    string_topic = Node(
            package='py_pubsub',
            executable='talker',
        )

    # ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
    twist_topic = ExecuteProcess(
                cmd=[
                    "ros2",
                    "topic",
                    "pub",
                    "--rate", "1",
                    "/turtle1/cmd_vel",
                    "geometry_msgs/msg/Twist",
                    "{linear: {x: 3.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
                ],
            )

    # ros2 topic pub /int16_topic std_msgs/msg/Int16 "data: 28"
    int16_topic = ExecuteProcess(
                cmd=[
                    "ros2",
                    "topic",
                    "pub",
                    "/int16_topic",
                    "std_msgs/msg/Int16",
                    "data: 35"
                ],
            )

    # ros2 topic pub /bool_topic std_msgs/msg/Bool "data: True"
    bool_topic = ExecuteProcess(
                cmd=[
                    "ros2",
                    "topic",
                    "pub",
                    "/bool_topic",
                    "std_msgs/msg/Bool",
                    "data: True"
                ],
            )


    return LaunchDescription([
        background_r_launch_arg,
        background_g_launch_arg,
        background_b_launch_arg,
        turtlesim,
        web_video_server,
        rosbridge,
        camera,
        string_topic,
        twist_topic,
        int16_topic,
        bool_topic
    ])
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription

from launch_ros.actions import Node


def generate_launch_description():
    urdf = os.path.join(
        get_package_share_directory('reachy_description'),
        'reachy.URDF',
    )

    rviz_config = os.path.join(
        get_package_share_directory('reachy_description'),
        'reachy.rviz',
    )

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            arguments=[urdf],
        ),
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            parameters=[
                {'-d', rviz_config},
            ],
        ),
    ])

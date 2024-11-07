import os
import xacro

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, GroupAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, Command
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # # Declare the argument to optionally enable Gazebo
    # use_gazebo = DeclareLaunchArgument(
    #     'use_gazebo', default_value='false',
    #     description='Set to "true" to launch Gazebo along with robot state publisher and RViz.'
    # )
 
    # # Define the path to the URDF file
    # robot_description_content = Command([
    #     PathJoinSubstitution([
    #         FindPackageShare('xacro'), 'xacro'
    #     ]),
    #     ' ',
    #     PathJoinSubstitution([
    #         FindPackageShare('my_pkg'), 'description', 'robot.urdf'
    #     ])
    # ])

    # # Robot State Publisher Node
    # robot_state_publisher_node = Node(
    #     package='robot_state_publisher',
    #     executable='robot_state_publisher',
    #     name='robot_state_publisher',
    #     output='screen',
    #     parameters=[{'robot_description': robot_description_content}]
    # )

    # RViz Node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=[
            '-d', PathJoinSubstitution([
                FindPackageShare('my_pkg'), 'config', 'robot_config.rviz'
            ])
        ]
    )

    # # Gazebo launch (optional)
    # gazebo_group = GroupAction([
    #     IncludeLaunchDescription(
    #         PythonLaunchDescriptionSource(
    #             PathJoinSubstitution([
    #                 FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py'
    #             ])
    #         ),
    #         launch_arguments={'world': PathJoinSubstitution([
    #             FindPackageShare('my_pkg'), 'worlds', 'empty_world.sdf'
    #         ])}.items()
    #     ),
    #     Node(
    #         package='gazebo_ros',
    #         executable='spawn_entity.py',
    #         name='spawn_entity',
    #         output='screen',
    #         arguments=[
    #             '-entity', 'two_wheeled_robot',
    #             '-file', PathJoinSubstitution([
    #                 FindPackageShare('my_pkg'), 'description', 'robot.urdf'
    #             ])
    #         ]
    #     )
    # ], condition=IfCondition(LaunchConfiguration('use_gazebo')))


    pkg_path = os.path.join(get_package_share_directory('my_pkg'))
    xacro_file = os.path.join(pkg_path,'description','robot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file)
    
    # Create a robot_state_publisher node
    params = {'robot_description': robot_description_config.toxml()}
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',     
        output='screen',
        parameters=[params]
    )


    # Create and return launch description
    return LaunchDescription([
        # use_gazebo,
        # robot_description_content,
        # robot_state_publisher_node,
        rviz_node,
        node_robot_state_publisher,
        # gazebo_group
    ])

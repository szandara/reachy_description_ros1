import os
from glob import glob

from setuptools import setup


package_name = 'reachy_description'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name), glob('launch/*.py')),

        (os.path.join('share', package_name), [
            'reachy.URDF', 'reachy.URDF.xacro',
        ]),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.dae')),

        (os.path.join('share', package_name), ['reachy.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Pollen-Robotics',
    maintainer_email='contact@pollen-robotics.com',
    description='ROS2 Foxy description package for the Reachy robot',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

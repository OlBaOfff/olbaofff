ros2 run turtlesim turtlesim_node
clear
ls
cat
cat Új\ Szöveges\ dokumentum.txt 
locale # check for UTF-8
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt upgrade
sudo apt install ros-humble-desktop
sudo apt install ros-dev-tools
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_py talker
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
sudo apt install libxml2-dev libraw1394-dev libncurses5-dev qtcreator swig sox espeak cmake-curses-gui cmake-qt-gui git subversion gfortran libcppunit-dev libqt5xmlpatterns5-dev python3-osrf-pycommon libasound2-dev libgl1-mesa-dev xorg-dev python3-vcstool python3-colcon-common-extensions python3-pykdl python3-pyudev libxml2-dev libraw1394-dev libncurses5-dev qtcreator swig sox espeak cmake-curses-gui cmake-qt-gui git subversion gfortran libcppunit-dev libqt5xmlpatterns5-dev libbluetooth-dev ros-humble-joint-state-publisher* ros-humble-xacro gfortran-9
sudo apt update
sudo apt install terminator
cd ~/ros2_ws
code .
sudo apt install terminator -y
ros2 run turtlesim turtle_teleop_key
ros2 run turtlesim_fraktal fraktal
cd ~/ros2_ws
colcon build --packages-select turtlesim_fraktal
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
ros2 pkg list | grep turtlesim_fraktal
ros2 run turtlesim_fraktal fraktal
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
source install/setup.bash
sudo apt update
sudo apt install ros-humble-turtlesim
ros2 pkg executables turtlesim
ros2 run turtlesim turtlesim_node
cd src
ros2 pkg create --build-type ament_python turtlesim_fraktal --dependencies rclpy turtlesim
clear
sudo apt update
sudo apt install ros-humble-rclpy ros-humble-geometry-msgs -y
source /opt/ros/humble/setup.bash
clear
cd ros2_ws
cd ~/ros2_ws
colcon build
ros2 run turtlesim_fraktal fraktal
source install/setup.bash
colcon build
ros2 run turtlesim_fraktal fraktal
chmod +x fraktal_node.py
clear
cd ~/ros2_ws/src
rm -rf turtlesim_fraktal
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python turtlesim_fraktal --dependencies rclpy turtlesim geometry_msgs
cd ~/ros2_ws/src/turtlesim_fraktal
mkdir turtlesim_fraktal
touch turtlesim_fraktal/fraktal_node.py
chmod +x turtlesim_fraktal/fraktal_node.py
code turtlesim_fraktal/fraktal_node.py
clear
cd ~/ros2_ws
colcon build
ros2 run turtlesim turtlesim_node
source install/setup.bash
ros2 run turtlesim turtlesim_node
ros2 run turtlesim_fraktal fraktal
ros2 pkg list | grep turtlesim_fraktal
ros2 run turtlesim_fraktal fraktal
colcon build
ros2 run turtlesim_fraktal fraktal
git ad
git add
ros2 run turtlesim turtlesim_node

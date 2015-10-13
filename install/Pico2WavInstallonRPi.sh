#uncomment the second source deb
sudo nano /etc/apt/sources.list
sudo apt-get update
sudo apt-get install fakeroot debhelper automake autoconf libtool help2man libpopt-dev hardening-wrapper
mkdir pico_build
cd pico_build
apt-get source libttspico-utils
cd svox-1.0+git20110131
dpkg-buildpackage -rfakeroot -us -uc
cd ..
sudo dpkg -i libttspico-data_1.0+git20110131-2_all.deb
sudo dpkg -i libttspico0_1.0+git20110131-2_armhf.deb
sudo dpkg -i libttspico-utils_1.0+git20110131-2_armhf.deb
echo  "Pico2Wave has been installed on your Raspberry Pi!"

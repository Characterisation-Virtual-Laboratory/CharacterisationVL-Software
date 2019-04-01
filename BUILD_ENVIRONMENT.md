# Instructions for creating a singularity build machine on cloud



## Singularity installation
The build environment is setup as follow:
1. Create virtual machine (NeCTAR 2-4 cores, Ubuntu 16.04)
2. Install dependencies for singularity and functionality

sudo apt install build-essential ubuntu-desktop vim libarchive-dev xfce4 xfce4-goodies

The build machine will need to have a functional X configuration. To access this X server remotely the suggested tool is x2go. Installation and training instructions can be found here: http://training.nectar.org.au/package07/sections/connectWithX2Go.html
### To install x2go
sudo add-apt-repository ppa:x2go/stable

sudo apt-get install x2goserver x2goserver-xsession

3. Download and install singularity
wget https://github.com/singularityware/singularity/releases/download/2.6.0/singularity-2.6.0.tar.gz

tar xf singularity-2.6.0.tar.gz

cd singularity-2.6.0

./configure

make -j

sudo make install 

4. Run build commands to use an alternative tmp directory by setting environment variables for root

sudo mkdir -p /mnt/tmp

sudo chown ubuntu /mnt/tmp

sudo SINGULARITY_TMPDIR=/mnt/tmp singularity build XXX.img XXX.def |tee build`date +%R-%F`.log

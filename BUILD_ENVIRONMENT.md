The build environment is setup as follow:
1. Create virtual machine (NeCTAR 2-4 cores, Ubuntu 16.04)
2. Install dependencies for singularity and functionality


sudo apt install build-essential
sudo apt install ubuntu-desktop vim
sudo apt install libarchive-dev


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

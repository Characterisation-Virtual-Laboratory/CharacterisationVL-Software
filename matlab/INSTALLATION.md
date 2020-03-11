# Installation Procedure

## Prerequisites:
* MATLAB Offline Installer ISO
* MATLAB File Installation Key
* MATLAB license file
* Singularity 3

# Installation Procedure
* Create a matlab folder: `mkdir matlab`
* Mount the ISO: `mount -o rw matlab<VERSION>.iso matlab`
* Copy the File Installation Key and the license file into the matlab folder
* Edit `matlab/installation_input.txt` to use the FIK and license files
* Build the container: `sudo singularity build Singularity.MATLAB matlab.sif`

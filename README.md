# CharacterisationVL-Software
The purpose of this repository is for storing definition files to submit to singularity hub.

Each software package is located in its own folder. The files are tagged with the software name and version number or date of build.

To add software to the repository you will need to create a new branch. The new branch will be checked and merged.

## Steps to add a software package
1. Create a branch
```
$ git branch <software name>
```
2. Make a subdirectory
3. Add all the necessary files
 * Singularity definition file or installation script
 * Readme file including install and testing notes
 * Desktop files for adding to menus with necessary tags
4. Commit all changes, including a helpful message
5. Check singularity hub for completed build.
```
$ git commit -m "<software name> added as requested in support ticket"
```
5. Submit merge request


## Running GUI applications on a non-GPU node
The applications in the Singularity container should run without the need for a dedicated GPU.

However, an X server needs to be running for this to work. On nodes with GPU, X Server is started with NVIDIA driver, and on non-GPU nodes, the X Server is started with MESA library.

X Server can be started during boot (for example, using `systemctl set-default graphical.target`).

Make sure that VirtualGL package is installed in the container. The code below will download and install VirtualGL.

```
wget https://swift.rc.nectar.org.au/v1/AUTH_810/CVL-Singularity-External-Files/virtualgl_2.6.2_amd64.deb

dpkg -i virtualgl_2.6.2_amd64.deb
```

The application startup script doesn't need to be modified, however, if the application needs to be manually started, then `vglrun` needs to be appended before running the application. For example: `singularity exec --nv -B /projects:/projects -B /scratch:/scratch /usr/local/chimerax/0.8/chimerax.sif vglrun ChimeraX`




[![https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg](https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg)](https://singularity-hub.org/collections/1396)

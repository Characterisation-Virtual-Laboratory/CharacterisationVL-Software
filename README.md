# CharacterisationVL-Software
The purpose of this repository is for storing definition files to submit to [Singularity Hub.](https://singularity-hub.org/)

If you are new to Singularity containers, please refer to [https://sylabs.io/guides/3.5/user-guide/](https://sylabs.io/guides/3.5/user-guide/) or a newer version of this documentation.

Each software package is located in its own folder. The files are tagged with the software name and version number or date of build. Please read below for the naming convention.

To add software to the repository you will need to create a new branch. The new branch is the name of the software product. By convention, the new branch will be checked and merged into the master branch and then deleted.

## Steps to add a software package
1. Clone this repository
2. Create a branch
```
$ git branch <software name>
```
3. Make a subdirectory for the software product.
```
$ mkdir <software name>
```
4. Add all the necessary files.
 * Singularity definition file or installation script
 * Readme file including install and testing notes
 * Desktop files for adding to menus with necessary tags
 * For full details, [please refer to the 'template' folder in this repository.](template/README.md)
4. Commit all changes, including a helpful message
```
$ git commit -m "<software name> added as requested in support ticket"
```
6. Push to the remote repository. i.e. this one.
7. Submit merge request

## Naming your Singularity definition file, Singularity Hub and Licensing
For all Singularity recipes where the software licensing permits redistribution, please use this naming convention:

```
   Singularity.applicationName_version
   Singularity.applicationName_version-cuda-cudaVersion

```

This is where Singularity Hub fits into the equation. There is a webhook between this repository and [Singularity Hub](https://singularity-hub.org/). When a commit is merged into the master branch, Singularity Hub will build the container.

If successfully built, the path to the container on Singularity Hub is:

```
  singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:applicationName_version
  singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:applicationName_version-cuda-cudaVersion

```

For software where licensing does not support redistribution, the container recipe can still be defined, but the container should not be built on Singularity Hub.

An example on how to handle this situation is the recipe for CCP-EM.
The [README.md](CCP_EM/README.md) contains a section on Prerequisites. This section lists the required files to build the container. The license must be accepted by the end user to obtain them.

Prerequisite files should not be committed to this repository.

To prevent Singularity Hub from attempting to build the container, we simply use a different recipe naming convention as follows:

```
   applicationName_version.def
   applicationName_version-cuda-cudaVersion.def

```

## Ubuntu Base Images
The folder 'ubuntu-base-image' contains recipes for pre built base containers. These can be used as a starting point to aid/speed up the development of your container recipe.

The current versions are built using Ubuntu 18.04 LTS, plus Cuda 9 or Cuda 10.1 if required.

These are available on Singularity Hub.

For example: from the Graphviz Singularity.graphviz-2.40.1 recipe

```
Bootstrap: shub
From:      Characterisation-Virtual-Laboratory/CharacterisationVL-Software:1804
```

These two lines, will tell Singularity to use the 'shub' bootstrap to obtain the '1804' ubuntu-base-image container from Singularity Hub.

From here you just need to add the requirements to build a container for your required piece of software. Please see [Singularity.graphviz-2.40.1](graphviz/Singularity.graphviz-2.40.1)
for the full recipe.

The current ubuntu-base-images include Python, VirtualGL and TurboVNC plus Cuda if indicated in the name.



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

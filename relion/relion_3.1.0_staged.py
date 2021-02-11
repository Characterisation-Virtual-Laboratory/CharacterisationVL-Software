from hpccm.building_blocks import apt_get, gnu
from hpccm.primitives import baseimage, copy, environment, label, runscript, shell

## Prerequisite:
#  - HPCCM - https://github.com/NVIDIA/hpc-container-maker
#  - Singularity >= v 3.2 to support the staged build.
#  - MotionCor2_1.4.0.zip - https://msg.ucsf.edu/software
#  - Gctf_v1.06_and_examples.tar.gz - https://www2.mrc-lmb.cam.ac.uk/research/locally-developed-software/zhang-software/
#  - ctffind-4.1.14-linux64.tar.gz  - https://www2.mrc-lmb.cam.ac.uk/research/locally-developed-software/zhang-software/
##
# hpccm --recipe relion_3.1.0_staged.py
#        --format singularity
#        --singularity-version 3.5 > recipe.def

# Start "base recipe, known as '18.04_cuda10'"
# add docstring to Dockerfile
Stage0 += comment(__doc__.strip(), reformat=False)

Stage0.name = '18.04_cuda10'
Stage0 += baseimage(image="ubuntu:18.04", _as=Stage0.name)

# Setting up environment vars for container build and runtime.
Stage0 += environment(variables={"LC_ALL": "en_AU.UTF-8", "LANGUAGE": "en_AU.UTF-8"})

# Set apt repos and packages to install
base_packages = apt_get(
    repositories=[
        "deb http://us.archive.ubuntu.com/ubuntu/ bionic main restricted",
        "deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates main restricted",
        "deb http://us.archive.ubuntu.com/ubuntu/ bionic universe",
        "deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates universe",
    ],
    ospackages=[
        "software-properties-common",
        "locales",
        "wget",
        "ubuntu-desktop",
        "vim",
        "git",
        "cmake",
        "freeglut3-dev",
        "build-essential",
        "libx11-dev",
        "libxmu-dev",
        "libxi-dev",
        "libglu1-mesa",
        "libglu1-mesa-dev",
        "libxft-dev",
        "libxft2",
        "libfreetype6",
        "libfreetype6-dev",
        "python-pip",
        "python-pyqt5",
        "pyqt5-dev",
        "python-tk",
        "dirmngr",
        "gpg-agent"
    ],
)
Stage0 += base_packages

# Install gnu compiler v6
compiler = gnu(fortran=False, version="6")
Stage0 += compiler

# Upgrade ubuntu packages
Stage0 += shell(commands=["apt upgrade -y"])
Stage0 += shell(
    commands=[
        "locale-gen en_AU.UTF-8",
        "mkdir -p /tmp/cuda10",
        "cd /tmp/cuda10",
        "wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.1.168-1_amd64.deb",
        "dpkg -i cuda-repo-ubuntu1804_10.1.168-1_amd64.deb",
        "apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub",
        "apt-get update",
        "apt install -y cuda-10-1"
    ]
)

# Adding in Relion 3.1.0, build from source code.
Stage0 += apt_get(ospackages=["libopenmpi-dev", "libopenmpi2", "libfftw3-dev", "libtiff-dev"])
Stage0 += shell(
    commands=[
        "mkdir -p /opt/buildRelion",
        "mkdir -p /opt/relion-3.1.0",
        "cd /opt/buildRelion",
        "git clone -b 3.1.0 https://github.com/3dem/relion.git",
        "cd relion",
        "mkdir build",
        "cd build",
        "cmake -DCMAKE_INSTALL_PREFIX=/opt/relion-3.1.0 ..",
        "make -j 1",
        "make install",
    ]
)

# Adding MotionCor2 - local copy required, licensing prevents redistribution
Stage0 += copy(src="MotionCor2_1.4.0.zip", dest='/opt/MotionCor2_1.4.0.zip')
Stage0 += shell(commands=["cd /opt/",
                          "unzip MotionCor2_1.4.0.zip",
                          "rm MotionCor2_1.4.0.zip",
                          "chmod -R g+rx,o+rx MotionCor2_1.4.0"])

# Adding Gctf - needs to be downloaded as a pre requisite. The website no longer supports using wget.
Stage0 += copy(src="Gctf_v1.06_and_examples.tar.gz", dest="/opt/Gctf_v1.06_and_examples.tar.gz")
Stage0 += shell(commands=["cd /opt",
                          "tar -zxvf Gctf_v1.06_and_examples.tar.gz"])

# Adding ctffind - needs to be downloaded as a pre requisite. The website no longer supports using wget.
Stage0 += copy(src="ctffind-4.1.14-linux64.tar.gz", dest="/opt/ctffind-4.1.14/ctffind-4.1.14-linux64.tar.gz")
Stage0 += shell(commands=["cd /opt/ctffind-4.1.14",
                          "tar -zxvf ctffind-4.1.14-linux64.tar.gz"])

Stage0 += shell(commands=["mkdir -p /opt/resmap",
                          "cd /opt/resmap",
                          "wget https://downloads.sourceforge.net/project/resmap/ResMap-1.1.4-linux64",
                          "chmod +x ResMap-1.1.4-linux64"])

###############################################################################
# Release stage
###############################################################################
Stage1.name = 'final'
Stage1 += baseimage(image="ubuntu:18.04", _as=Stage1.name)
Stage1 += Stage0.runtime(_from=Stage0.name)

Stage0 += label(
    metadata={"MAINTAINER": "jay.vanschyndel@monash.edu", "HARDWARE": "gpu"}
)

# Setting up post environment vars. _export=False indicates these are only setup for container runtime
Stage1 += environment(
    variables={
        "CUDABINPATH": "/usr/local/cuda-10.1/bin",
        "CUDALIBPATH": "/usr/local/cuda-10.1/lib64/stubs:/usr/local/cuda-10.1/lib64/:/usr/local/cuda-10.1/lib",
        "MOTIONCOR2BINPATH": "/opt/MotionCor2_1.4.0",
        "GCTFBINPATH": "/opt/Gctf_v1.06/bin",
        "CTFFINDBINPATH": "/opt/ctffind-4.1.14/bin",
        "RESMAPBINPATH": "/opt/resmap",
        "RELION_QSUB_EXTRA_COUNT": "2",
        "RELION_QSUB_EXTRA2": "time",
        "RELION_QSUB_EXTRA2_DEFAULT": "16:00:00",
        "RELION_QSUB_EXTRA1": "account",
        "RELION_QSUB_EXTRA1_DEFAULT": "account",
        "RELION_QSUB_TEMPLATE": "/usr/local/relion/3.1.0/scripts/Submit_template_1xNode_2xK80.sh",
        "RELION_MOTIONCOR2_EXECUTABLE": "/opt/MotionCor2_1.4.0/MotionCor2_1.4.0_Cuda101",
        "RELION_CTFFIND_EXECUTABLE": "/opt/ctffind-4.1.14/bin/ctffind",
        "RELION_GCTF_EXECUTABLE": "/opt/Gctf_v1.06/bin/Gctf-v1.06_sm_30_cu8.0_x86_64",
        "RELION_RESMAP_EXECUTABLE": "/opt/resmap/ResMap-1.1.4-linux64",
        "RELIONBINPATH": "/opt/relion-3.1.0/bin",
        "RELIONLIBPATH": "/opt/relion-3.1.0/lib:/usr/local/cuda/lib64:/usr/lib/x86_64-linux-gnu/openmpi/lib"
    },
    _export=False,
)
Stage1 += environment(
    variables={
        "PATH": "$RESMAPBINPATH:$GCTFBINPATH:$CTFFINDBINPATH:$MOTIONCOR2BINPATH:$RELIONBINPATH:$CUDABINPATH:$PATH",
        "LD_LIBRARY_PATH": "$RELIONLIBPATH:$CUDALIBPATH:$LD_LIBRARY_PATH",
    },
    _export=False,
)

# Setting up environment vars for container build and runtime.
Stage1 += environment(variables={"LC_ALL": "en_AU.UTF-8", "LANGUAGE": "en_AU.UTF-8"})

Stage1 += shell(commands=["apt upgrade -y"])

release_packages = apt_get(
    repositories=[
        "deb http://us.archive.ubuntu.com/ubuntu/ bionic main restricted",
        "deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates main restricted",
        "deb http://us.archive.ubuntu.com/ubuntu/ bionic universe",
        "deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates universe",
    ],
    ospackages=["software-properties-common",
                "locales",
                "ubuntu-desktop",
                "freeglut3",
                "openmpi-bin",
                "libtiff5",
                "tcsh",
                "libfftw3-3",
                "libfltk-gl1.3",
                "libx11-6",
                "libxmu6",
                "libxi6",
                "libglu1-mesa",
                "libxft2",
                "libfreetype6",
                "wget",
                "ca-certificates",
                "ssl-cert",
                "dirmngr",
                "gpg-agent",
                "evince",
                "openssh-server"])
Stage1 += release_packages


#Installing virtualGl and TurboVNC
Stage1 += shell(
    commands=[
        "cd /tmp",
        "wget https://swift.rc.nectar.org.au/v1/AUTH_810/CVL-Singularity-External-Files/turbovnc_2.1.2_amd64.deb",
        "dpkg -i turbovnc_2.1.2_amd64.deb",
        "wget https://swift.rc.nectar.org.au/v1/AUTH_810/CVL-Singularity-External-Files/virtualgl_2.6.2_amd64.deb",
        "dpkg -i virtualgl_2.6.2_amd64.deb"])

# Installing cuda 10.1
Stage1 += shell(
    commands=[
        "locale-gen en_AU.UTF-8",
        "mkdir -p /tmp/cuda10",
        "cd /tmp/cuda10",
        "wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.1.168-1_amd64.deb",
        "dpkg -i cuda-repo-ubuntu1804_10.1.168-1_amd64.deb",
        "apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub",
        "apt-get update",
        "apt install -y cuda-10-1",
        "echo '*** Cuda 8 to 10.1 fudge - enables Gctf to run. ***'",
        "cd /usr/local/cuda/lib64/",
        "ln -s libcufft.so.10 libcufft.so.8.0"
    ])

# Relion
Stage1 += copy(_from=Stage0.name,
               src='/opt/relion-3.1.0/bin',
               dest='/opt/relion-3.1.0/bin')
Stage1 += copy(_from=Stage0.name,
               src='/opt/relion-3.1.0/lib',
               dest='/opt/relion-3.1.0/lib')

# MotionCor2
Stage1 += copy(_from=Stage0.name,
               src='/opt/MotionCor2_1.4.0',
               dest='/opt/MotionCor2_1.4.0')

# Gctf
Stage1 += copy(_from=Stage0.name,
               src='/opt/Gctf_v1.06/bin',
               dest='/opt/Gctf_v1.06/bin')

# ctffind
Stage1 += copy(_from=Stage0.name,
               src='/opt/ctffind-4.1.14/bin',
               dest='/opt/ctffind-4.1.14/bin')

# ResMap
Stage1 += copy(_from=Stage0.name,
               src='/opt/resmap',
               dest='/opt/resmap')

Stage1 += runscript(commands=["$*"])

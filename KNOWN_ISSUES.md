Errors during container build

If container build results in "no space left on device" this is from writing to the /tmp folder and/or the home folder on the root filesystem. To fix this error set the environment variable SINGULARITY_TMPDIR to another location. See build instructions for further details in this repository or the singularity instructions https://www.sylabs.io/guides/2.6/user-guide/build_environment.html
